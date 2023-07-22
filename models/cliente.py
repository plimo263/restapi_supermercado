from extensios import db


class ClienteModel(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(80), unique = True, nullable = False)
    nome = db.Column(db.String(100), nullable = False)
    senha = db.Column(db.String(80), nullable = False)
