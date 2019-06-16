from django.core.management import BaseCommand
import requests
import sqlite3
from tqdm import tqdm
from rates.models import BaseCurrency, Currency

def fetch_currency(url, db_name):
	conn = sqlite3.connect(db_name)
	c = conn.cursor()
	data = requests.get(url)
	data = data.json()
	rates = data['rates']
	for curr in tqdm(rates):
		#print( f"{curr} {data['base']} {rates[curr]} {data['date']}" )
		try:
			c.execute("INSERT INTO rates_currency (id, symbol, base, rate_to_gbp, date) VALUES (null, ?, ?, ?, ?)", (curr, data['base'], rates[curr], data['date']))
		except Exception as e:
			conn.rollback()
			print("failed")
	try:
		c.execute("INSERT INTO rates_basecurrency (id, symbol, date) VALUES (null, ?, ?)", (data['base'], data['date']))
	except Exception as e:
		conn.rollback()
		print("failed")
	finally:
		conn.commit()


class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('string', nargs=2, type=str)

	def handle(self, *args, **kwargs):
		date = kwargs['string'][0]
		currency = kwargs['string'][1]
		url = f"https://api.exchangeratesapi.io/{date}?base={currency}"
		print(url)
		db = 'db.sqlite3'
		try:
			fetch_currency(url, db)
			self.stdout.write(self.style.SUCCESS("Data imported successfully."))
		except Exception as e:
			self.stdout.write(self.style.SUCCESS(f"Error. {e}"))
