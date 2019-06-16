from django.db import models

class Currency(models.Model):
	symbol = models.CharField(max_length=3)
	base = models.CharField(max_length=3)
	rate_to_gbp = models.DecimalField(max_digits=15, decimal_places=5)
	date = models.DateField(auto_now=False, auto_now_add=False)

class BaseCurrency(models.Model):
	symbol = models.CharField(max_length=3)
	date = models.DateField(auto_now=False, auto_now_add=False)
	#currencies = models.ManyToManyField(Currency)
