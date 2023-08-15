from marshmallow import fields, Schema, validate, ValidationError
from models import ItemModel

def validate_item_exists(id_item: int):
    ''' Realiza a validação para ver se o item existe no sistema '''
    item = ItemModel.query.filter(
        ItemModel.id == id_item
    ).first()

    if not item:
        raise ValidationError(f"Item não encontrado usano este id {id_item!r}")


messages = {
    'nome': {
        'invalid': 'O nome deve ter ao menos 2 caracteres',
        'required': 'O nome é requerido para cadastro de item'
    },
    'valor': {
        'invalid': 'O valor deve ser um número de ponto flutuante',
        'required': 'O valor do item é requerido.'
    }
}

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(dump_only=True)
    valor = fields.Float(dump_only=True)

class ItemAddSchema(Schema):
    nome = fields.Str( validate = validate.Length(min = 2), error_messages=messages['nome'], required = True)
    valor = fields.Float(required = True)

class ItemUpdSchema(Schema):
    id = fields.Int(validate=validate_item_exists, required=True)
    nome = fields.Str( validate = validate.Length(min = 2), error_messages=messages['nome'], required = True)
    valor = fields.Float(required = True)

class ItemDelSchema(Schema):
    id = fields.Int(validate=validate_item_exists, required=True)