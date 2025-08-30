from django.db import models
from django.core.validators import MinValueValidator
from pyexpat.errors import messages


class Expirationsystem(models.Model):
    reference_code = models.IntegerField(verbose_name="Referência", null=False, blank=False, validators=[MinValueValidator(1, message="O valor não pode ser menor ou igual a zero!")])
    product = models.CharField(verbose_name="Produto", max_length=100, null=False, blank=False)
    expiration_date = models.DateField(verbose_name="Validade", null=False, blank=False)
    quantity = models.IntegerField(verbose_name="Quantidade", null=True, blank=True)
