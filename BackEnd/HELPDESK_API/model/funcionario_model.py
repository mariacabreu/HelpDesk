# Column define colunas da tabela
# Integer, String, Enum e Boolean são tipos de dados do banco
# equivalente aos tipos usados com @Column no JPA
from sqlalchemy import Column, Integer, String, Enum, Boolean

# Base é a classe base das entidades
# equivalente ao uso de @Entity no JPA
from HELPDESK_API.config.database import Base

# biblioteca do Python para criar enums
# equivalente ao enum no Java
import enum


# Enum de cargos do funcionário
# equivalente a: enum Cargo { REDE, HARDWARE, SOFTWARE, SISTEMA }
class Cargo(enum.Enum):

    REDE = "Rede"
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    SISTEMA = "Sistema"


# Enum para níveis de suporte
class NivelSuporte(enum.Enum):

    N1 = "N1"
    N2 = "N2"
    N3 = "N3"


# Enum para status do funcionário
class StatusFuncionario(enum.Enum):

    ATIVO = "Ativo"
    INATIVO = "Inativo"


# Classe que representa a tabela do banco
# equivalente a uma entidade JPA
# @Entity
class FuncionarioModel(Base):

    # nome da tabela no banco
    # equivalente a @Table(name="tab_funcionarios")
    __tablename__ = "tab_funcionarios"


    # chave primária da tabela
    # equivalente a:
    # @Id
    # @GeneratedValue
    id = Column(Integer, primary_key=True)


    # nome do funcionário
    # equivalente a @Column(nullable=false)
    nome = Column(String(100), nullable=False)


    # cpf único
    # unique=True impede duplicação no banco
    # equivalente a @Column(unique=true)
    cpf = Column(String(11), unique=True, nullable=False)


    # cargo usando enum
    cargo = Column(Enum(Cargo))


    # nível de suporte
    nivel_suporte = Column(Enum(NivelSuporte))


    # departamento da empresa
    departamento = Column(String(100))


    # email único
    email = Column(String(150), unique=True)


    # telefone
    telefone = Column(String(20))


    # ramal interno
    ramal = Column(String(10))


    # login do sistema
    # no seu projeto login = email
    login = Column(String(150), unique=True)


    # senha do usuário
    senha = Column(String(255))


    # status do funcionário
    status = Column(Enum(StatusFuncionario))


    # jornada de trabalho
    jornada_trabalho = Column(String(50))


    # define se pode receber chamados
    # default=True significa que o valor padrão é verdadeiro
    pode_receber_chamado = Column(Boolean, default=True)