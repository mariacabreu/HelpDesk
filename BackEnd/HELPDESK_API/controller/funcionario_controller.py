# APIRouter cria um conjunto de rotas
# equivalente ao @RestController do Spring
from fastapi import APIRouter, Depends

# Session representa a sessão do banco
# parecido com o EntityManager/Hibernate Session
from sqlalchemy.orm import Session

# Importa a sessão do banco criada na configuração
from HELPDESK_API.config.database import SessionLocal

# Importa a camada de regras de negócio
# equivalente ao @Service no Spring
from HELPDESK_API.service.funcionario_service import FuncionarioService

# DTO usado para receber dados da requisição
# equivalente a um DTO no Java
from HELPDESK_API.dto.funcionario_request_dto import FuncionarioRequestDTO


# Cria o controller de funcionários
# prefix define a rota base
# equivalente a @RequestMapping("/funcionarios")
router = APIRouter(prefix="/funcionarios")


# Instancia o service
# equivalente ao @Autowired FuncionarioService
service = FuncionarioService()


# Função que cria e fecha a conexão com o banco
# FastAPI injeta ela automaticamente nas rotas
# parecido com injeção de dependência do Spring
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota GET para listar funcionários
# equivalente a @GetMapping
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return service.listar_funcionarios(db)


# Rota POST para salvar funcionário
# equivalente a @PostMapping
@router.post("/")
def salvar(funcionario: FuncionarioRequestDTO, db: Session = Depends(get_db)):
    return service.salvar_funcionario(db, funcionario)


# Rota DELETE para deletar funcionário
# equivalente a @DeleteMapping("/{id}")
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    service.deletar_funcionario(db, id)
    return {"mensagem": "Funcionário deletado"}