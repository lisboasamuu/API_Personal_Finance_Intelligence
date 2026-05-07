from flask import Flask
from src.core.config import Config
from src.core.database import db
from src.api.routes.health import health_bp
from src.api.routes.insigths import insights_bp
from src.api.routes.summary import summary_bp
from src.api.routes.transactions import transaction_bp

def create_app():
    #criação do app a partir de uma config ja inicialmente feita e inicialização do banco de dados
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    #registro dos blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(insights_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(transaction_bp)

    with app.app_context():
        db.create_all()
    return app
