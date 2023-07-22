from extensios import db

class LojaModel(db.Model):
    __tablename__ = 'loja'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80), nullable = False)
