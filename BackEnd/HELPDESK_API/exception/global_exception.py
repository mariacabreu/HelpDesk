# Request representa a requisição HTTP recebida
from fastapi import Request

# JSONResponse permite retornar respostas JSON personalizadas
from fastapi.responses import JSONResponse

# FastAPI é a aplicação principal
from fastapi import FastAPI

# ValidationError ocorre quando um DTO recebe dados inválidos
# equivalente às validações do Bean Validation no Spring
from pydantic import ValidationError


# Cria uma exceção personalizada da aplicação
# equivalente a criar uma CustomException no Java
class ApiException(Exception):

    # construtor que recebe a mensagem do erro
    def __init__(self, mensagem: str):
        self.mensagem = mensagem


# Função que registra os tratadores de erro na aplicação
# parecido com @ControllerAdvice no Spring Boot
def add_exception_handlers(app: FastAPI):


    # trata erros do tipo ApiException
    @app.exception_handler(ApiException)
    async def api_exception_handler(request: Request, exc: ApiException):

        return JSONResponse(
            status_code=400,
            content={
                "erro": exc.mensagem
            }
        )


    # trata erros de validação do Pydantic
    # acontece quando o DTO recebe dados inválidos
    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request: Request, exc: ValidationError):

        return JSONResponse(
            status_code=422,
            content={
                "erro": "Erro de validação",
                "detalhes": exc.errors()
            }
        )


    # trata qualquer erro não previsto
    # equivalente a ExceptionHandler global no Spring
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):

        return JSONResponse(
            status_code=500,
            content={
                "erro": "Erro interno do servidor",
                "detalhe": str(exc)
            }
        )