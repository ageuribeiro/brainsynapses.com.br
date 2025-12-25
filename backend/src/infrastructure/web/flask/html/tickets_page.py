from flask import Blueprint, render_template
from src.application.listar_tickets import listar_tickets


tickets_page = Blueprint('tickets_page', __name__)

@tickets_page.get('/api/tickets')
def page():
    return render_template('tickets.html', tickets=listar_tickets())