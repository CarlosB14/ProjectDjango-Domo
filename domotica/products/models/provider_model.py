from django.db import models
from django.contrib.auth.models import User




class Provider(models.Model):
    name = models.CharField(verbose_name='name',max_length=200)
    address = models.CharField(verbose_name='address',max_length=300)
    city = models.CharField(verbose_name='city',max_length=100, null=True, blank=True)
    country = models.CharField(verbose_name='country',max_length=100, null=True, blank=True)
    cod_postal = models.CharField(verbose_name='cod_postal',max_length=20, null=True, blank=True)
    phone = models.CharField(verbose_name='phone',max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='email',)
    web = models.URLField(verbose_name='web',null=True, blank=True)

    def __str__(self):
        return self.name