from django.db import models


class Operation(models.Model):
    """ Operation class"""
    number_1 = models.DecimalField(max_digits=20, decimal_places=1)
    number_2 = models.DecimalField(max_digits=20, decimal_places=1)
    result = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
