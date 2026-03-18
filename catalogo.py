from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

#Criar uma classe de filmes
#Colunas = id, titulo, genero, ano_lancamento, nota, disponivel

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False) 
    genero = Column(String(100), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    nota = Column(Float) 
    disponivel = Column(Boolean, default=True)

    def __init__(self, titulo, genero, ano, nota):
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano
        self.nota = nota
        
    #Função para imprimir
    def __repr__(self):
        return f"Filme = id={self.id} - nome={self.titulo} - genero={self.genero}"



#Conexão com o banco
engine = create_engine("sqlite:///catalogo_filmes.db")

#Criar as tabelas
Base.metadata.create_all(engine)

#Crio fábrica de sessões no banco
Session = sessionmaker(bind=engine)

#Funções do CRUD
def cadastrar_filme():
    print(f"\n--- CADASTRAR FILMES ---\n")
    titulo = input("Digite o nome do filme: ")
    genero = input("Digite o gênero do filme: ")
    ano = int(input("Digite o ano de lançamento do filme: "))
    nota = float(input("Digite a nota do filme: "))

    with Session() as session:
        try:
            filmes_existentes = session.query(Filme).filter_by(titulo=titulo, ano_lancamento=ano).first()
            if filmes_existentes == None:
                novo_filme = Filme(titulo, genero, ano, nota)
                session.add(novo_filme) 
                session.commit()
            else:
                print(f"Já existe um filme cadastrado com esse título e ano")
        except Exception as erro:
            session.rollback()
            print(f"OCorreu um erro {erro}")

#Chamar a função
# cadastrar_filme()

#Criar a função listar e função deletar

#Listar

with Session() as session:
    try:
        filmes = session.query(Filme).all()
        for user in filmes:
            print(f"Nome: {user.titulo} - Gênero: {user.genero} - Ano: {user.ano_lancamento} - Nota: {user.nota}")
    except Exception as erro:
        session.rollback()
        print(f"Ocorreu um {erro}")



