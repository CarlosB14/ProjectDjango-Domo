from django.db import models
from django.contrib.auth.models import User

from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField


class Services(models.Model):
    title = models.CharField(verbose_name='title',max_length=200)
    description = RichTextField(verbose_name='description')
    show_home = models.BooleanField(
        'Mostrar en la home',
        default=False
    )
    services_image = ImageField(
        verbose_name = "Imagen Servicios",
        upload_to = "services/images/",
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(verbose_name='title',max_length=200)
    description = RichTextField(verbose_name='description')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title