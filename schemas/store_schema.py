from marshmallow import fields, Schema, validate, ValidationError
from models import StoreModel

messages = {
    'name': {
        'invalid': 'O nome da loja não foi enviado corretamente',
        'required': 'Necessário enviar o nome da loja',
    },
    'store': {
        'invalid': 'O id da loja informada não existe',
        'required': 'Necessário enviar o id da loja',
    }
}

def validate_store_exists(id_store: int):
    ''' Verifica se a loja existe no sistema '''
    store = StoreModel.query.filter(StoreModel.id == id_store).first()
    if not store:
        raise ValidationError('O id da loja enviada não existe no sistema.')

class StoreSchema(Schema):
    id = fields.Int(validate=validate_store_exists, required=True, error_messages=messages['store'])
    nome = fields.Str(required=True)

class StorePostSchema(Schema):
    nome = fields.Str(validate=validate.Length(min=2) ,required=True, error_messages=messages['name'])

class StoreDelSchema(Schema):
    id = fields.Int(validate=validate_store_exists, required=True, error_messages=messages['store'])