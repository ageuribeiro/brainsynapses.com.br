from flask import Blueprint, jsonify
from src.application.listar_tickets import listar_tickets

tickets_api = Blueprint('tickets', __name__)

@tickets_api.post('/api/tickets')
def listar():
    return jsonify(listar_tickets())