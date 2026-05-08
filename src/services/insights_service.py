from datetime import *
from src.models.transaction import Transaction
from src.core.database import db

def get_insights():
    today = date.today()
    current_month = today.month
    current_year = today.year

    if current_month == 1:
        prev_month = 12
        prev_year = current_year - 1
    else:
        prev_month = current_month - 1
        prev_year = current_year
    current_transactions = Transaction.query.filter(
        db.extract('year', Transaction.date) == current_year,
        db.extract('month', Transaction.date) == current_month
    ).all()
    prev_transactions = Transaction.query.filter(
        db.extract('year', Transaction.date) == prev_year,
        db.extract('month', Transaction.date) == prev_month    
    )
    #Criando uma lista para armazenar os insights e definindo suas lógicas, como gasto total e onde maior gastou.
    insights_list = []
    total_current = sum(t.amount for t in current_transactions)
    if total_current > 0:
        food_spent = sum(t.amount for t in current_transactions if t.category == 'alimentação')
        if food_spent / total_current > 0.3:
            insights_list.append('Você gastou muito com alimentação este mês')
    transport_current = sum(t.amount for t in current_transactions if t.category == 'transporte')
    prev_transport = sum(t.amount for t in prev_transactions if t.category == 'transporte')
    if prev_transport > 0 and transport_current > prev_transport:
        insights_list.append('Transporte aumentou em relação ao mês passado')

    if not insights_list:
        insights_list.append('Nenhum insight relevante no momento')
        
    return insights_list