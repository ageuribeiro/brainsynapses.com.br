from flask import Blueprint, jsonify
from src.infrastructure.persistence.mongodb.product_repository import MongoDBProductRepository
from src.infrastructure.persistence.mongodb.client import get_db

products_api = Blueprint('products_api', __name__)

@products_api.get('/api/products')
def list_products_endpoint():
    db = get_db()
    product_repository = MongoDBProductRepository(db['products'])
    products = product_repository.list_all_products()
    return jsonify(products)