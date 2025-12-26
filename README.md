# User Management API

API REST para gerenciamento de usuários desenvolvida com **FastAPI** e **PostgreSQL**, incluindo autenticação JWT e controle de acesso por rota.

Projeto focado em demonstrar boas práticas de desenvolvimento backend, organização em camadas, validação de dados e segurança.

---

## Tecnologias

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

## Funcionalidades

- Cadastro de usuários
- Autenticação via JWT
- Proteção de rotas com OAuth2
- Hash seguro de senhas
- Validação de dados com Pydantic
- CRUD completo de usuários
- Documentação automática com Swagger/OpenAPI

---

## Estrutura do Projeto

```
user-management-api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── deps.py
│   ├── database.py
│   ├── config.py
│   └── routes/
│       ├── users.py
│       └── auth.py
├── requirements.txt
└── README.md
```

---

## Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/userdb
SECRET_KEY=super-secret-key
```

---

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

Acesse:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

---

## Exemplos de Uso

### Criar usuário

`POST /users`

```json
{
  "email": "admin@example.com",
  "password": "123456"
}
```

---

### Login

`POST /login`

Utilize **form-data**:
- username: email
- password: senha

Resposta:
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

### Listar usuários (rota protegida)

`GET /users`

Necessário header:
```
Authorization: Bearer <token>
```

---

## Status do Projeto

✔ Projeto finalizado  
✔ Pronto para portfólio e currículo  
✔ Compatível com vagas de estágio backend Python  

---

## Autor

Gabriel Rubiali  
Estudante de Ciência da Computação  
Backend Python
