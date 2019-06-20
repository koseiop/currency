from django.core.management import BaseCommand
import requests
import sqlite3
import datetime
from tqdm import tqdm
from rates.models import BaseCurrency, Currency

def fetch_currency(url, db_name):
	conn = sqlite3.connect(db_name)
	c = conn.cursor()
	data = requests.get(url)
	data = data.json()
	rates = data['rates']
	try:
		c.execute("INSERT INTO rates_basecurrency (id, symbol, date) VALUES (null, ?, ?)", (data['base'], data['date']))
		conn.commit()
		add_currency(data, rates, db_name)
	except Exception as e:
		print(e)
		conn.rollback()
		print("failed")


def add_currency(original_data, currency_dict, db_name):
	conn = sqlite3.connect(db_name)
	c = conn.cursor()
	base_curr = BaseCurrency.objects.get(symbol=original_data['base'], date=original_data['date'])
	for curr in tqdm(currency_dict):
		try:
			print(f"Adding {curr}, {currency_dict[curr]}")
			c.execute("INSERT INTO rates_currency (id, symbol, base_id, rate_to_base, date) VALUES (null, ?, ?, ?, ?)", (curr, base_curr.id, currency_dict[curr], original_data['date']))
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
		currency = kwargs['string'][1].upper()
		date_obj = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:]))
		print(date_obj)
		try:
			if BaseCurrency.objects.get(symbol=currency, date__icontains=date):
				print(f"Data for currency {currency} on {date} already exists.\nAborting script")
		except Exception:
			print(f"Data for currency {currency} on {date} will be added.")
			url = f"https://api.exchangeratesapi.io/{date}?base={currency}"
			print(url)
			db = 'db.sqlite3'
			try:
				fetch_currency(url, db)
				self.stdout.write(self.style.SUCCESS("Data imported successfully."))
			except Exception as e:
				print(e)
				self.stdout.write(self.style.SUCCESS(f"Error. {e}"))
