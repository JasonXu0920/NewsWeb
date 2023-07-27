from django.db import models

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField()