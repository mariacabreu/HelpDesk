# BaseModel é usado para criar DTOs no FastAPI
# ele define o formato da resposta da API
# equivalente a um DTO no Java
from pydantic import BaseModel


# DTO de resposta do funcionário
# define quais dados serão enviados para o cliente
# equivalente a um Response DTO no Spring
class FuncionarioResponseDTO(BaseModel):

    # id do funcionário
    # equivalente ao id da entidade
    id: int

    # nome do funcionário
    nome: str

    # email do funcionário
    email: str

    # cargo do funcionário
    cargo: str

    # nível de suporte
    nivel_suporte: str