from collections import defaultdict
from src.models.transaction import Transaction

def get_summary():
    transactions = Transaction.query.all()
    total = sum(t.amount for t in transactions)
    by_category = defaultdict(float)
    for t in transactions:
        by_category[t.category] += t.amount
    return {
        'total': round(total, 2),
        #dict comprehension para filtrar num 2 a 2 de categorias um resumo de cada
        'por_categoria': {cat:round(val, 2) for cat, val in by_category.items() }
    }