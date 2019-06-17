import datetime

print(datetime.datetime.today().strftime("%Y-%m-%d"))
today = str(datetime.datetime.today().strftime("%Y-%m-%d"))
print (today)

url = 'https://api.exchangeratesapi.io/2019-06-15'

print( str(url[-10:]) )
