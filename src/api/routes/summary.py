from flask import Blueprint, jsonify
from src.services.summary_service import *

summary_bp = Blueprint('summary', __name__)

@summary_bp.get('/summary')
def summary():
    return jsonify(get_summary())