from django.db import models


class Expirationsystem(models.Model):
    reference_code = models.IntegerField(verbose_name="Referência", null=False, blank=False)
    product = models.CharField(verbose_name="Produto", max_length=100, null=False, blank=False)
    expiration_date = models.DateField(verbose_name="Validade", null=False, blank=False)
    quantity = models.IntegerField(verbose_name="Quantidade", null=True, blank=True)
