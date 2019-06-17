import requests
import json
import datetime

url = 'https://api.exchangeratesapi.io/2019-06-15'
data = requests.get(url)


data = data.json()

date = str(url[-10:])

#json.dump(data, open(date +".txt", 'w'))
print(date)
