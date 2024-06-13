class Usuario():
    def __init__(self,nome,email,nivel):
        self.__nome = nome
        self.__email = email
        self.__nivel = nivel

 




   
      



"""
 id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    email  = db.Column(db.String(200))
    fk_nivel_id= db.Column(db.Integer,db.ForeignKey('nivel.id'))
    nivel = relationship("Nivel",back_populates="usuarios")
"""