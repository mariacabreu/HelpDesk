# Session é a sessão do banco
# equivalente ao EntityManager/Hibernate Session
from sqlalchemy.orm import Session

# Importa o repository que acessa o banco
# equivalente ao JpaRepository no Spring
from HELPDESK_API.repository.funcionario_repository import FuncionarioRepository

# Importa o model (entidade do banco)
# equivalente ao @Entity no JPA
from HELPDESK_API.model.funcionario_model import FuncionarioModel

# Importa o DTO que recebe dados da API
# equivalente ao DTO usado no @RequestBody
from HELPDESK_API.dto.funcionario_request_dto import FuncionarioRequestDTO


# Classe de regras de negócio
# equivalente a um @Service no Spring
class FuncionarioService:


    # construtor da classe
    # cria uma instância do repository
    # no Spring seria @Autowired
    def __init__(self):
        self.repository = FuncionarioRepository()


    # lista todos os funcionários
    # chama o repository para buscar no banco
    def listar_funcionarios(self, db: Session):

        return self.repository.listar(db)


    # salva um novo funcionário
    # contém regras de negócio antes de salvar
    def salvar_funcionario(self, db: Session, dto: FuncionarioRequestDTO):


        # verifica se já existe funcionário com esse email
        # equivalente a findByEmail no Spring
        funcionario_existente = self.repository.buscar_por_email(db, dto.email)


        # regra de negócio: email não pode repetir
        if funcionario_existente:
            raise Exception("E-mail já cadastrado")


        # cria um novo objeto da entidade
        # equivalente a new Funcionario()
        novo = FuncionarioModel()


        # copia os dados do DTO para o Model
        # equivalente a setters no Java
        novo.nome = dto.nome
        novo.cpf = dto.cpf
        novo.cargo = dto.cargo
        novo.nivel_suporte = dto.nivel_suporte
        novo.departamento = dto.departamento
        novo.email = dto.email
        novo.telefone = dto.telefone
        novo.ramal = dto.ramal


        # regra do sistema:
        # login será o mesmo valor do email
        novo.login = dto.email


        # senha do usuário
        novo.senha = dto.senha

        # status do funcionário
        novo.status = dto.status

        # jornada de trabalho
        novo.jornada_trabalho = dto.jornada_trabalho

        # define se pode receber chamados
        novo.pode_receber_chamado = dto.pode_receber_chamado


        # envia para o repository salvar no banco
        return self.repository.salvar(db, novo)


    # deleta um funcionário
    def deletar_funcionario(self, db: Session, id: int):


        # busca o funcionário pelo id
        funcionario = self.repository.buscar_por_id(db, id)


        # regra: funcionário precisa existir
        if not funcionario:
            raise Exception("Funcionário não encontrado")


        # chama o repository para deletar
        self.repository.deletar(db, funcionario)