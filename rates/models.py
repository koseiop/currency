from django.db import models

class Currency(models.Model):
    symbol = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=15, decimal_places=5)
