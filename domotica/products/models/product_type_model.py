from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Product_type(models.Model):
    name = models.CharField(verbose_name='name',max_length=200)
    description = RichTextField(verbose_name='description')

    def __str__(self):
        return self.name