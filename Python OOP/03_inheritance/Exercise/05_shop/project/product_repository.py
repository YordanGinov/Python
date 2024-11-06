from typing import Optional

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((p for p in self.products if p.name == product_name), None)
        # try:
        #     product = [el for el in self.products if el.name == name][0]
        #     return product
        # except IndexError:
        #     pass

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
