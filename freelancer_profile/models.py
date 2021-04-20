from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Freelancer(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    url = models.URLField(_("URL"), max_length=200)
    phone = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
