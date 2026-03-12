from fastapi import APIRouter
from HELPDESK_API.controller.funcionario_controller import router as funcionario_router

router = APIRouter()

router.include_router(funcionario_router)