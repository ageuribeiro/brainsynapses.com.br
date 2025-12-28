from flask import Blueprint, render_template
from src.application.listar_tickets import Category


tickets_page = Blueprint('tickets_page', __name__)

@tickets_page.get('/api/tickets')
def page():
    return render_template('tickets.html', tickets=Category.tickets())