from apps.core.models import BaseModel

from django.db import models


class Product(BaseModel):
    """
    Set products information in database
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)
