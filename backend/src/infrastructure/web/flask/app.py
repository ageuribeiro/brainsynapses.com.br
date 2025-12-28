from flask import Flask
from flask_cors import CORS
from .api.tickets_api import tickets_api
from .api.products_api import products_api
from .html.tickets_page import tickets_page

def create_app():
    app = Flask(__name__, template_folder='src/infrastructure/public/templates', static_folder='src/infrastructure/public/static')
    CORS(app)

    app.register_blueprint(tickets_api)
    app.register_blueprint(tickets_page)

    return app