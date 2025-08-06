from fastapi import FastAPI
from app import models, routes, db

app = FastAPI()

models.Base.metadata.create_all(bind=db.engine)

app.include_router(routes.router)