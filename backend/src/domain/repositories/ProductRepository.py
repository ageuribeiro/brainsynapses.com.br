from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def update_product(self, product):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass

    @abstractmethod
    def list_all_products(self):
        pass    