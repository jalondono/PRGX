from django.db import models


class Operation(models.Model):
    """ Operation class"""
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
