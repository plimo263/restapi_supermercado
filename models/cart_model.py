from extensios import db


class CartModel(db.Model):
    __tablename__ = "carrinho"

    id = db.Column(db.Integer, primary_key = True)
    id_item = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
