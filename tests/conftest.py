import os
import tempfile
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app.db import Base
from ..app.main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def test_db_url():
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    db_url = f"sqlite:///{db_path}"
    yield db_url
    os.close(db_fd)
    os.remove(db_path)

@pytest.fixture(scope="session")
def engine(test_db_url):
    engine = create_engine(test_db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(engine):
    TestingSessionLocal = sessionmaker(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture()
def client(db_session, monkeypatch):
    from app import routes

    def override_get_db():
        yield db_session

    app.dependency_overrides[routes.get_db] = override_get_db
    return TestClient(app)
