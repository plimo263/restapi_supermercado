from flask_smorest import Blueprint, abort 
from flask.views import MethodView
from models import StoreModel
from extensios import db
from sqlalchemy.exc import IntegrityError

from schemas.store_schema import StoreSchema, StorePostSchema, StoreDelSchema
from schemas.success_schema import SuccessSchema

blp = Blueprint('store', __name__, description='API de comunicação com as lojas')

@blp.route('/store')
class StoreView(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        ''' Recupera todas as lojas do sistema'''

        return StoreModel.query.all()
    
    @blp.arguments(StorePostSchema)
    @blp.response(200, StoreSchema)
    def post(self, item_data):
        ''' Cria uma nova loja no sistema'''

        store_new: StoreModel = StoreModel(
            nome = item_data['nome']
        )

        try:
            db.session.add(store_new)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(400, message=f"A loja {item_data['nome']!r} ja existe")

        return store_new

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def put(self, item_data):
        ''' Atualiza uma determinada loja no sistema'''
        store: StoreModel = StoreModel.query.filter(
            StoreModel.id == item_data['id']
        ).first()
        store.nome = item_data['nome']

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(400, message=f"A loja {item_data['nome']!r} ja existe")

        return store
    
    @blp.arguments(StoreDelSchema)
    @blp.response(200, SuccessSchema)
    def delete(self, item_data):
        ''' Exclui uma determinada loja do sistema'''
        store: StoreModel = StoreModel.query.filter(
            StoreModel.id == item_data['id']
        ).first()
        
        try:
            db.session.delete(store)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            abort(400, message=f"Erro ao tentar excluir a loja {item_data['nome']!r}.")

        return {'sucesso': 'Loja excluida com sucesso.'}