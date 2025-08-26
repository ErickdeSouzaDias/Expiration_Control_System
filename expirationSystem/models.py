from django.db import models


class Expirationsystem(models.Model):
    reference_code = models.IntegerField(null=False, blank=False)
    product = models.CharField(max_length=100, null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    quantity = models.IntegerField(null=True, blank=True)
