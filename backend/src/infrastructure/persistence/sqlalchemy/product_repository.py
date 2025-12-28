from src.domain.repositories.ProductRepository import ProductRepository
from src.domain.entities.Product import Product
from .models import ProductModel
from .session import SessionLocal   

class SQLAlchemyProductRepository(ProductRepository):
    def save(self, product: Product):
        session = SessionLocal()
        model = ProductModel(
            id=product.id,
            name=product.name,
            price=product.price
        )
        session.add(model)
        session.commit()
        session.close()

    def list(self):
        session = SessionLocal()
        models = session.query(ProductModel).all()
        session.close()

        return [
            Product(m.id, m.name, m.price)
            for m in models
        ]