from flask import Blueprint, jsonify
#por convêniencia utilizamos a blueprint por profissionalismo
health_bp = Blueprint('health', __name__)
#criando a rota para checar saude da api e dando um json como mensagem
@health_bp.get('/health')
def health():
    return jsonify({'status': 'ok'})