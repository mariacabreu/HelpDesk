# OBS: depois de ter feito o passo a passo a partir de (# 📌 HelpDesk),
# sempre que for rodar o código vá para o terminal aberto pelo Downloads
# ou onde está a pasta, já com o MySQL aberto, e digite:

cd HelpDesk\BackEnd

# Depois

.venv\Scripts\activate

# Se ativar certo vai aparecer assim no terminal, como no exemplo:

(.venv) C:\Users\joaoo\Downloads\HelpDesk\BackEnd>

# Depois é só rodar a API

uvicorn HELPDESK_API.app:app --reload

# LocalHost FastApi

http://127.0.0.1:8000/docs

# Banco de Dados

CREATE DATABASE BDD_SWIFTDESK;

USE BDD_SWIFTDESK;

SHOW DATABASES;

# 📌 HelpDesk

Projeto de sistema HelpDesk desenvolvido utilizando **FastAPI**.

## 🚀 FastAPI
Framework moderno e rápido para criação de APIs com Python.
Ele permite criar aplicações web de forma simples, com alta performance e documentação automática.

---

## 📂 Passo a Passo para Criar o Projeto

```bash
# Criar a pasta do projeto
mkdir nome_do_projeto
# Cria um novo diretório onde ficará o projeto

# Entrar na pasta do projeto
cd nome_do_projeto
# Acessa a pasta criada

# Criar o ambiente virtual
python -m venv .venv
# Cria um ambiente virtual chamado .venv para isolar as dependências do projeto

# Ativar o ambiente virtual (Linux / Mac)
source .venv/bin/activate
# Ativa o ambiente virtual no terminal

# Ativar o ambiente virtual (Windows - CMD)
.venv\Scripts\activate
# Ativa o ambiente virtual no Windows usando CMD

# Ativar o ambiente virtual (Windows - PowerShell)
.venv\Scripts\Activate.ps1
# Ativa o ambiente virtual no Windows usando PowerShell

# Depois disso você pode instalar o FastAPI (versão recomendada)
pip install "fastapi[standard]"
# Instala o FastAPI com as dependências recomendadas

# Após a instalação do FastAPI, dentro do projeto principal crie uma nova pasta chamada HELPDESK_API
# Essa será a pasta principal da API

# Dentro de HELPDESK_API crie o arquivo __init__.py
# Esse arquivo é usado para o Python identificar a pasta como um módulo do projeto

# Depois crie o arquivo app.py
# Esse será o arquivo principal da aplicação (equivalente ao main no Java)

# Crie uma pasta chamada tests
# Pasta utilizada para armazenar os testes do projeto

# Crie um arquivo chamado pyproject.toml
# Arquivo usado para configurar o projeto e organizar as ferramentas utilizadas
```

---

## ⚙️ Conteúdo do arquivo pyproject.toml

```toml
[project]
name = "fast-helpdesk"
version = "0.1.0"
description = ""
authors = [
    { name = "João Vítor", email = "mjoaooliveira7891@gmail.com" },
    { name = "Maria Clara", email = "" },
    { name = "Pedro Matias", email = "" }
]
```

---

## 📄 No arquivo `app.py` adicione:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## ▶️ Executando o servidor

Com o `.venv` ativado, execute no terminal:

```bash
fastapi dev HELPDESK_API\app.py
```

Depois acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 📘 Documentação automática (Swagger)

Por padrão, o FastAPI já disponibiliza a documentação automática em:

```
http://127.0.0.1:8000/docs
```

O Swagger é uma ferramenta usada para documentar e testar APIs, mas não é a documentação completa do software.

No Swagger é possível:

- Ver todas as rotas da API
- Testar as requisições
- Enviar dados
- Ver as respostas
- Ver os modelos de dados

---

## 🔵 Código síncrono
Executa uma coisa de cada vez.  
Cada operação precisa terminar antes da próxima começar.

## 🟢 Código assíncrono
Permite executar outras tarefas enquanto espera uma operação demorada terminar, melhorando a performance em APIs.

---

HELPDESK_API
│
├── __pycache__   cria automatico depois de um tempo  
├── config/       adiciona pasta  
├── controller/   adiciona pasta  
├── dto/          adiciona pasta  
├── exception/    adiciona pasta  
├── model/        adiciona pasta  
├── repository/   adiciona pasta  
├── service/      adiciona pasta  
├── __init__.py   adiciona arquivo  
├── app.py        adiciona arquivo  
└── routers.py    adiciona arquivo  

---

## 📂 Arquivo `routers.py`

Crie um arquivo chamado `routers.py`.  
Ele serve para organizar as rotas da aplicação, separando as URLs da lógica principal (`app.py`).  

É como juntar as URLs e os controllers em um único local, deixando o projeto mais organizado.

---

# 🔗 Integração do Backend com Banco de Dados (MySQL)

Com o `venv` ativo, instale as dependências:

```bash
pip install sqlalchemy pymysql
```

---

## 📂 Criar arquivo de conexão

Criar em:

```
HELPDESK_API/config/database.py
```

```python
from sqlalchemy import create_engine
# Importa a função responsável por criar o "motor" de conexão com o banco de dados

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker → cria sessões (conexões ativas) para executar operações no banco
# declarative_base → cria a classe base que será usada para definir os modelos (tabelas)

# String de conexão com o banco de dados
# Formato: banco+driver://usuario:senha@host/nome_do_banco
DATABASE_URL = "mysql+pymysql://root:senha@localhost/helpdesk"

# Cria o engine (motor de conexão)
# Ele gerencia as conexões e faz a comunicação com o MySQL
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
# Cada sessão representa uma conexão ativa com o banco
SessionLocal = sessionmaker(
    autocommit=False,  # Não faz commit automático (você precisa chamar commit manualmente)
    autoflush=False,   # Não envia alterações automaticamente para o banco
    bind=engine        # Liga essa sessão ao engine criado acima
)

# Cria a classe base para os modelos (entidades)
# Todas as classes que representam tabelas devem herdar de Base
Base = declarative_base()
```
📁 config

Configurações do sistema.
Ex: conexão com o banco de dados.

📁 model

Representa as tabelas do banco.
Define campos, tipos e enums.
Equivalente ao Entity do Spring Boot.

📁 dto

Controla dados que entram e saem da API.

Request DTO → dados que o cliente envia

Response DTO → dados que a API retorna

📁 repository

Camada que acessa o banco de dados.
Faz consultas, salvar, deletar, buscar.

Equivalente ao JpaRepository.

📁 service

Onde ficam as regras de negócio.

Exemplo:

validar email duplicado

definir login = email

📁 controller

Camada das rotas da API.

Exemplo:

GET /funcionarios
POST /funcionarios
DELETE /funcionarios

Recebe requisição e chama o service.

📁 exception

Trata erros globais da API.

Exemplo:

email já cadastrado

erro interno

📄 routers.py

Centraliza todas as rotas do sistema.

📄 app.py

Arquivo principal da aplicação.

inicia o FastAPI

conecta banco

registra rotas