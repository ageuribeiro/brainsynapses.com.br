from src.domain.repositories.ProductRepository import ProductRepository

class MongoDBProductRepository(ProductRepository):
    def __init__(self, collection):
        self.collection = collection

    def save(self, product):
        self.collection.insert_one(product.to_dict())

    def list(self):
        return list(self.collection.find({}, {'_id': 0} ))