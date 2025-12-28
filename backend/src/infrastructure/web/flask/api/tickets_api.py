from flask import Blueprint, jsonify
from src.application.listar_tickets import Category

tickets_api = Blueprint('tickets_api', __name__)

@tickets_api.get('/api/tickets')
def listar():
    return jsonify(Category.tickets())