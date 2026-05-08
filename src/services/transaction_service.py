#A rota que enviar para cá vai ter toda a lógica por tras da transação. Seja exclusão, atualização, criação, listagem

from src.models.transaction import Transaction
from src.core.database import db
from src.services.categorization import classify_category
from datetime import datetime

#Criar a transação
def create_transaction(data):
    category = data.get('category') or classify_category(data['description'])
    transaction = Transaction(
        description=data['description'],
        amount=float(data['amount']),
        date = datetime.strptime(data['date'], '%Y-%m-%d').date(),
        category = category
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction
#Listagem das transações
def get_all_transaction(filters =  None):
    query = Transaction.query
    if filters:
        if 'category' in filters:
            query = query.filter_by(category=filters['category'])
        if 'date' in filters:
            year, month = map(int, filters['date'].split('-'))
            query = query.filter(
                db.extract('year', Transaction.date) ==  year,
                db.extract('month', Transaction.date) == month
            )
    return query.all()

def get_transaction_by_id(id):
    return Transaction.query.get(id)
#Pode retornar none se for o caso.
def update_transaction(transaction, data):
    if 'description' in data:
        transaction.description = data['description']
        if 'category' not in data:
            transaction.category = classify_category(data['description'])
    if 'amount' in data:
        transaction.amount = float(data['amount'])
    if 'date' in data:
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    if 'category' in data:
        transaction.category = data['category']
    db.session.commit()
    return transaction

def delete_transaction(transaction):
    db.session.delete(transaction)
    db.session.commit()