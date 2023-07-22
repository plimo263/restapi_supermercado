from extensios import db


class ItemModel(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80), unique = True, nullable = False)
    valor = db.Column(db.Float, nullable = False)
