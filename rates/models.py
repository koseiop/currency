from django.db import models

class Currency(models.Model):
	symbol = models.CharField(max_length=3)
	base = models.ForeignKey('BaseCurrency', on_delete=models.CASCADE)
	rate_to_base = models.DecimalField(max_digits=15, decimal_places=5)
	date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.symbol

class BaseCurrency(models.Model):
	symbol = models.CharField(max_length=3)
	date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.symbol
