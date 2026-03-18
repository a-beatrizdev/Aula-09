# Instalar o sqlalchemy
# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#Criar a classe base
Base = declarative_base()

#Como criar a tabela no banco
class Usuario(Base):
    __tablename__ = "usuarios"
    
    #Como criar uma coluna no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)
    #nullable =False > Campo obrigatório
    nome = Column(String(100), nullable=False) 
    # unique=True > Não permite e-mails repetidos
    email = Column(String(100), nullable=False, unique=True)
    idade = Column(Integer, nullable=False)
    salario = Column(Float) 
    ativo = Column(Boolean, default=True)


    #Metodo construtor
    def __init__(self, nome_usuario, email, idade, salario):
        self.nome = nome_usuario
        self.email = email
        self.idade = idade
        self.salario = salario
    

#Conexão com o banco
engine = create_engine("sqlite:///empresa.db")

#Criar as tabelas
Base.metadata.create_all(engine)

#Crio fábrica de sessões no banco
Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        #Buscar um usuário no banco
        usuario_existente = session.query(Usuario).filter_by(email="pedro@sp.senai.edu").first()
        if usuario_existente == None:
            #Como criar um objeto
            usuario1 = Usuario("Pedro", "pedro@sp.senai.edu", 29, 5000)

            session.add(usuario1)
            #Salvar no banco
            session.commit() 
        else:
            print(f"Já existe um usuário com esse e-mail")
    except Exception as erro:
        session.rollback()
        print(f"Ocorreu um {erro}")

#Usando o mesmo padrão with, faça agora para listar os usuários cadastrados no banco
with Session() as session:
    try:
        usuarios = session.query(Usuario).all()
        for user in usuarios:
            print(f"Nome: {user.nome} - Email: {user.email}")
    except Exception as erro:
        session.rollback()
        print(f"Ocorreu um {erro}")
        










