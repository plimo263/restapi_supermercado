from extensios import db
from sqlalchemy import func

class InvoiceModel(db.Model):
    __tablename__ = "nota_fiscal"

    id = db.Column(db.Integer, primary_key = True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable = False)
    id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'), nullable = False)
    data = db.Column(db.DateTime, default=func.now(), nullable = False)
