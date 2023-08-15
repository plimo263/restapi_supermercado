from extensios import db

class InvoiceItemModel(db.Model):
    __tablename__ = "nota_fiscal_item"

    id = db.Column(db.Integer, primary_key = True)
    id_item = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = False)
    id_nota = db.Column(db.Integer, db.ForeignKey('nota_fiscal.id'), nullable = False)
    sequencia = db.Column(db.Integer, nullable = False)
    valor_unitario = db.Column(db.Float(precision=2), nullable = False)
    valor_desconto = db.Column(db.Float(precision=2), nullable = False)
    valor_final = db.Column(db.Float(precision=2), nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
