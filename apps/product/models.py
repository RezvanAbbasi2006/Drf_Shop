from apps.core.models import BaseModel

from django.db import models


class ProductCategory(BaseModel):
    """
    Each product have one spacial category like digital for mobile
    """
    title = models.CharField(max_length=120, null=True)
    type = models.CharField(max_length=120, null=True)
    description = models.TextField(max_length=180, null=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    """
    Set product information in database
    """
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='product',
        null=True
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)
