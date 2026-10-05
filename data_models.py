# data_models.py
"""
Data model definitions for the Market Research CLI application.
Uses _slots_ for reduced memory overhead.
"""

class Product:
    # Explicitly define allowed attributes to restrict dynamic dict creation
    __slots__ = ('id', 'name', 'price', 'category', 'avg_score', 'review_count')

    def __init__(self, id: int, name: str, price: float, category: str, avg_score: float, review_count: int):
        self.id = int(id)
        self.name = str(name)
        self.price = float(price)
        self.category = str(category)
        self.avg_score = float(avg_score)
        self.review_count = int(review_count)

    def to_dict(self) -> dict:
        """Converts the Product object into a dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "avg_score": self.avg_score,
            "review_count": self.review_count
        }

    def _repr_(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, score={self.avg_score})"