class Product:
    """Класс для представления продукта."""
    name: str
    description: str
    price: float
    quantity: int

    # Переменная на уровне класса для подсчета количества продуктов
    product_count = 0

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1


class Category:
    """Класс для представления категории."""
    name: str
    description: str
    products: list

    # Переменная на уровне класса для подсчета количества категорий
    category_count = 0
    # Переменная на уровне класса для подсчета количества продуктов данной категории
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра класса"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count +=1

    def get_product_count(self) -> int:
        """Метод, который возвращает количество продуктов в категории"""
        return len(self.products)