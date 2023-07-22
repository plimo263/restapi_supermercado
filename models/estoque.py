from extensios import db


class EstoqueModel(db.Model):
    __tablename__ = "estoque"

    id = db.Column(db.Integer, primary_key = True)
    id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'), nullable = False)
    id_item = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = False)
    quantidade = db.Column(db.Integer, nullable = False, default = 0)
