# O que acontece aqui:
# recebe request
# valida com schema
# chama service
# retorna resposta

from flask import Blueprint, request, jsonify
from src.schemas.transaction_schema import validate_transaction
from src.services.transaction_service import *

transaction_bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@transaction_bp.post('')
def create():
    data = request.get_json() or {}
    errors =  validate_transaction(data)
    if errors:
        return jsonify({'erros': errors}), 400
    transaction = create_transaction(data)
    return jsonify(transaction.to_dict()), 201

@transaction_bp.get('')
def list_all():
    filters = {}
    #procure na request um argumento para category e date
    category = request.args.get('category')
    date = request.args.get('date')
    if category:
        filters['category'] =  category
    if date:
        try:
            year, month = map(int, date.split('-'))
        except ValueError:
            return jsonify({'error': 'formato de data inválido. Use YYYY-MM-DD'})
        filters['date'] = date
    transactions = get_all_transaction(filters)
    return jsonify([t.to_dict() for t in transactions])

@transaction_bp.get('/<int:id>')
def get_one(id):
    transaction = get_transaction_by_id(id)
    if not transaction:
        return jsonify("Transação não encontrada para o id selecionado"), 404
    return jsonify(transaction.to_dict())

@transaction_bp.put('/<int:id>')
def update(id):
    transaction = get_transaction_by_id(id)
    if not transaction:
        return jsonify({'error': 'transação não encontrada'}), 404
    data = request.get_json() or {}
    errors = validate_transaction(data, partial= True)
    if errors:
        return jsonify({'errors': errors}), 400
    updated_transaction = update_transaction(transaction, data)
    return jsonify(update_transaction.to_dict())
@transaction_bp.delete('/<int:id>')
def delete(id):
    transaction = get_transaction_by_id(id)
    if not transaction:
         return jsonify({'error': 'transação não encontrada'}), 404
    delete_transaction(transaction)
    return '', 204