from fastapi import FastAPI
from HELPDESK_API.routers import router
from HELPDESK_API.config.database import Base, engine
from HELPDESK_API.exception.global_exception import add_exception_handlers

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

# REGISTRA TRATAMENTO GLOBAL DE ERROS
add_exception_handlers(app)