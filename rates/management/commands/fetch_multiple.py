from django.core.management import BaseCommand
import requests
import sqlite3
import datetime
from tqdm import tqdm
from rates.models import BaseCurrency, Currency

curr_list = ['NZD', 'CAD', 'USD', 'AUD', 'HKD', 'GBP', 'EUR', 'CHF']

def fetch_multiple(url, db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    data = requests.get(url)
    data = data.json()
    rates = data['rates']
    for date in rates:
        date_obj = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:]))
        date_obj_text = date_obj.strftime("%A %d %b %Y")
        if (date_obj.strftime("%A") == "Saturday") or (date_obj.strftime("%A") == "Sunday"):
            print(f"{date_obj_text} falls on a weekend and contains Fridays data.\n Will not be added to database")
        else:
            try:
                if BaseCurrency.objects.get(symbol=data['base'], date=date):
                    print(f"Data for {data['base']} on {date_obj_text} already exists.\nSkipping")
            except Exception as e:
                try:
                    # No BaseCurrency object exists with symbol and date
                    c.execute("INSERT INTO rates_basecurrency (id, symbol, date) VALUES (null, ?, ?)", (data['base'], date))
                    conn.commit()
                    add_currency(data, rates[date], date, db_name)
                except Exception as e:
                    print(e)
                    conn.rollback()
                    print(f"failed on base, {e}")

def add_currency(original_data, currency_dict, date, db_name):
    conn = sqlite3.connect(db_name)
    c =  conn.cursor()
    base_curr = BaseCurrency.objects.get(symbol=original_data['base'], date=date)
    print(date)
    for curr in tqdm(currency_dict):
        try:
            print(f"Adding {curr}, {currency_dict[curr]}")
            c.execute("INSERT INTO rates_currency (id, symbol, base_id, rate_to_base, date) VALUES (null, ?, ?, ?, ?)", (curr, base_curr.id, currency_dict[curr], date))
        except Exception as e:
            conn.rollback()
            print(f"failed on currency, {e}")
        finally:
            conn.commit()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('string', nargs=3, type=str)

    def handle(self, *args, **kwargs):
        date1 = kwargs['string'][0]
        date2 = kwargs['string'][1]
        currency = kwargs['string'][2].upper()
        symbol_str = ""
        while len(curr_list) > 0:
            for i in curr_list:
                if len(curr_list) > 1:
                    symbol_str += i+","
                    curr_list.remove(i)
                else:
                    symbol_str += i
                    curr_list.remove(i)
        # if currency == "EUR":
        #     url = f'https://api.exchangeratesapi.io/history?start_at={date1}&end_at={date2}&symbols={symbol_str}'
        # else:
        #     url = f'https://api.exchangeratesapi.io/history?base={currency}&start_at={date1}&end_at={date2}&symbols={symbol_str}'
        url = f'https://api.exchangeratesapi.io/history?base={currency}&start_at={date1}&end_at={date2}&symbols={symbol_str}'
        print(url)
        db = 'db.sqlite3'
        try:
            fetch_multiple(url, db)
            self.stdout.write(self.style.SUCCESS("Data imported successfully."))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS(f"Error. {e}"))
