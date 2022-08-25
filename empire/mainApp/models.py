from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=100, blank=True)