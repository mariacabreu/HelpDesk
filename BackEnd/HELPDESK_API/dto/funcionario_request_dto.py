# BaseModel é a base dos DTOs no FastAPI
# ele valida automaticamente os dados recebidos
# equivalente a um DTO com validação no Java
from pydantic import BaseModel, EmailStr

# Enum cria valores fixos permitidos
# equivalente ao enum no Java
from enum import Enum


# Enum para os cargos do funcionário
# igual a: enum Cargo { REDE, HARDWARE, SOFTWARE, SISTEMA }
class CargoEnum(str, Enum):

    REDE = "Rede"
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    SISTEMA = "Sistema"


# Enum para nível de suporte
# equivalente a enum no Java
class NivelSuporteEnum(str, Enum):

    N1 = "N1"
    N2 = "N2"
    N3 = "N3"


# Enum para status do funcionário
class StatusEnum(str, Enum):

    ATIVO = "Ativo"
    INATIVO = "Inativo"


# DTO usado para receber dados da requisição
# equivalente a uma classe DTO no Java
# usada no @RequestBody
class FuncionarioRequestDTO(BaseModel):

    # nome do funcionário
    nome: str

    # cpf do funcionário
    cpf: str

    # cargo (usa enum definido acima)
    cargo: CargoEnum

    # nível de suporte
    nivel_suporte: NivelSuporteEnum

    # departamento da empresa
    departamento: str

    # email validado automaticamente
    # EmailStr garante que seja um email válido
    email: EmailStr

    # telefone
    telefone: str

    # ramal interno
    ramal: str

    # senha de acesso
    senha: str

    # status do funcionário
    status: StatusEnum

    # jornada de trabalho
    jornada_trabalho: str

    # define se pode receber chamados
    pode_receber_chamado: bool