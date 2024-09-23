from django.db import models

from .provider_model import Provider
from .product_type_model import Product_type

from ckeditor.fields import RichTextField


class Product(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200,
        )

    description = RichTextField(
        verbose_name='description',
        )

    providers = models.ManyToManyField(
        Provider,
        blank=True,
        )

    product_type = models.ForeignKey(
        Product_type,
        verbose_name='product_type',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )

    price = models.DecimalField(
        verbose_name="price",
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )
    product_firm = models.FileField(
        verbose_name = "Firmeware producto",
        upload_to = "products/firmwares/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name