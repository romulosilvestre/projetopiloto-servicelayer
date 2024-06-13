from app.models import nivel_model
from app import db

#cinco métodos
#listar dos níveis, listar um nivel, cadastrar
#alterar e excluir

#começando pelo pesquisar
def listar_niveis():
    niveis = nivel_model.Nivel.query.all()
    return niveis

def listar_nivel_id(id):
    nivel = nivel_model.Nivel.query.filter_by(id=id).first()  # Consulta todos os registros na tabela Nivel
    return nivel
def adicionar_nivel(nivel):
    db.session.add(nivel)
    db.session.commit()


