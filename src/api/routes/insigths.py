from flask import Blueprint, jsonify
from src.services.insights_service import get_insights

insights_bp = Blueprint('insights', __name__)
@insights_bp.get('/insights')
def insights():
    return jsonify(get_insights())