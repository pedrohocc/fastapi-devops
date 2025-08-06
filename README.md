# fastapi-devops

Este projeto foi desenvolvido para a disciplina de **DEVOPS**, com o objetivo de simular um pipeline de **CI/CD utilizando GitHub Actions**.

Para isso, utilizei o **FastAPI**, um framework web moderno em Python que explorei pela primeira vez. No projeto, implementei uma rota simples de `users`, incluindo um teste unitário para o endpoint de criação (`POST /users`).

## 🚀 Etapas do CI/CD

O pipeline de CI/CD segue as etapas solicitadas no material da disciplina:

- ✅ **Trigger** (em push/pull request na branch `main`)
- ✅ **Checkout do repositório**
- ✅ **Instalação das dependências**
- ✅ **Execução dos testes**
- ✅ **Build da aplicação**
- ✅ **Deploy simulado**

## 🧪 Testes

Foi criado um teste unitário para verificar a funcionalidade da rota `POST /users`, garantindo que o pipeline de CI funcione corretamente.

## 🛠️ Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) – framework web moderno e rápido para APIs com Python
- [Pytest](https://docs.pytest.org/) – framework de testes em Python
- [GitHub Actions](https://docs.github.com/actions) – automação de CI/CD

---

Este projeto tem como foco principal demonstrar o funcionamento básico de integração contínua e entrega contínua em um ambiente de desenvolvimento Python com FastAPI.

## Na Prática

Enfrentei alguns de problemas para ajustar a raiz do projeto em um primeiro momento. Posterior a isso, houve um loop ao executar o comando de "run" do FastApi no actions pelo fato de executar e continuar "ouvindo o terminal", porém solucionado com adição de alguns comando para verificar se está tudo ok!