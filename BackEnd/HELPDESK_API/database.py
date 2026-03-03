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