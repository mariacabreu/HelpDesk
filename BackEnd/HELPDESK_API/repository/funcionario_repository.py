# Session representa a sessão de acesso ao banco
# equivalente ao EntityManager/Hibernate Session no Java
from sqlalchemy.orm import Session

# Importa o model da tabela funcionarios
# equivalente à entidade JPA
from HELPDESK_API.model.funcionario_model import FuncionarioModel


# Classe Repository responsável por acessar o banco
# equivalente a um JpaRepository no Spring
class FuncionarioRepository:


    # Busca todos os funcionários
    # equivalente a findAll() do JpaRepository
    def listar(self, db: Session):

        return db.query(FuncionarioModel).all()


    # Busca funcionário pelo email
    # equivalente a findByEmail(String email)
    def buscar_por_email(self, db: Session, email: str):

        return db.query(FuncionarioModel)\
                 .filter(FuncionarioModel.email == email)\
                 .first()


    # Busca funcionário pelo id
    # equivalente a findById(Long id)
    def buscar_por_id(self, db: Session, id: int):

        return db.query(FuncionarioModel)\
                 .filter(FuncionarioModel.id == id)\
                 .first()


    # Salva um funcionário no banco
    # equivalente ao save() do JpaRepository
    def salvar(self, db: Session, funcionario: FuncionarioModel):

        # adiciona o objeto na sessão
        db.add(funcionario)

        # executa o INSERT no banco
        db.commit()

        # atualiza o objeto com dados do banco (ex: id gerado)
        db.refresh(funcionario)

        return funcionario


    # Deleta um funcionário
    # equivalente ao delete() do JpaRepository
    def deletar(self, db: Session, funcionario: FuncionarioModel):

        db.delete(funcionario)

        # executa DELETE no banco
        db.commit()