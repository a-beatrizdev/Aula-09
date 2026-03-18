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

