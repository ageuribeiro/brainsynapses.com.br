from flask import Blueprint, jsonify
from src.infrastructure.persistence.sqlalchemy.product_repository import SQLAlchemyProductRepository

from src.infrastructure.persistence.sqlalchemy.base import Base
from src.infrastructure.persistence.sqlalchemy.session import engine
from src.infrastructure.persistence.sqlalchemy.models import *

products_api = Blueprint('products_api', __name__)

@products_api.get('/api/products')
def list_products_endpoint():
    repo = SQLAlchemyProductRepository()
    products = repo.list()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'stock': p.stock
    } for p in products])

Base.metadata.create_all(bind=engine)