# representam a camada de dados e a lógica de negócios da aplicação. 
from src.core.database import db

class Transaction(db.Model):
    #model é um metodo do sqlalchemy para modelar dados relacionais.
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False, default='outros')
    # função para converter a dicionario
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'date': self.date.isoformat(),
            'category': self.category
        }