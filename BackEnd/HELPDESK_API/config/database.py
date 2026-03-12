# Cria a conexão com o banco de dados
# equivalente ao DataSource do Spring Boot
from sqlalchemy import create_engine

# Ferramentas do ORM do SQLAlchemy
# sessionmaker -> cria sessões de acesso ao banco (tipo EntityManager)
# declarative_base -> base para criar as entidades (tipo @Entity)
from sqlalchemy.orm import sessionmaker, declarative_base


# String de conexão com o banco
# equivalente ao spring.datasource.url
DATABASE_URL = "mysql+pymysql://root:@localhost/BDD_SWIFTDESK"


# Cria o motor de conexão com o banco
# parecido com o DataSource do Spring
engine = create_engine(DATABASE_URL)


# Cria a fábrica de sessões do banco
# cada sessão é usada para consultar, salvar ou deletar dados
# parecido com o EntityManager do JPA
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Classe base para todos os Models
# as entidades do banco herdam dela
# equivalente ao @Entity no JPA
Base = declarative_base()