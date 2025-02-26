from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text
from sqlalchemy.orm import relationship

#Holdai(MeuPai)
class Usuario(db.Model):
    __tablename__ = "usuario"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    email  = db.Column(db.String(200))
    fk_nivel_id= db.Column(db.Integer,db.ForeignKey('nivel.id'))
    nivel = relationship("Nivel",back_populates="usuarios")