from operator import itemgetter
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import IntegrityError
from extensios import db
from models import ItemModel, StoqModel
from schemas.item_schema import ItemSchema, ItemAddSchema, ItemUpdSchema, ItemDelSchema
from schemas.success_schema import SuccessSchema

blp = Blueprint('item', __name__, description='Interatividade com os itens')


@blp.route('/item')
class ItemView(MethodView):
    
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        ''' Retorna todos os itens cadastrados no sistema '''

        return ItemModel.query.all()
    
    @blp.arguments(ItemAddSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        ''' Cadastra um novo item no sistema '''

        nome, valor = itemgetter('nome', 'valor')(item_data)

        item: ItemModel = ItemModel(
            nome = nome,
            valor = valor
        )

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(400, message=f"O item {nome!r} já existe no sistema.")
        
        return item
    
    @blp.arguments(ItemUpdSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data):
        ''' Atualiza os dados de um item como nome ou valor '''

        id, nome, valor = itemgetter('id', 'nome', 'valor')(item_data)

        item: ItemModel = ItemModel.query.filter(
            ItemModel.id == id
        ).first()
        item.nome = nome 
        item.valor = valor

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            abort(400, message=f"O item com nome {nome!r} já existe no sistema.")
        
        return item
    
    @blp.arguments(ItemDelSchema)
    @blp.response(200, SuccessSchema)
    def delete(self, item_data):
        ''' Exclui o item do sistema, se nenhuma loja estiver com ele no estoque'''

        id = item_data['id']

        # Verifica se o item tem estoque em alguma loja
        if StoqModel.query.filter(
            StoqModel.id_item == id
        ).first():
            abort(400, message='Não é possível excluir o item pois existe estoque válido para ele em alguma loja')

        # Tudo certo pode recupera-lo para exclusao
        item: ItemModel = ItemModel.query.filter(
            ItemModel.id == id
        ).first()
        
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            abort(400, message=f"O item não pode ser excluido do sistema. Tente novamente mais")
        
        return {'sucesso': 'Item removido com sucesso'}




