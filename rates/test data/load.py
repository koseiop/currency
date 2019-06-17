import json

date = "2019-06-15"
data = json.load(open(f"{date}.txt"))
currency = 'GBP'
#print( f"1 {data['base']} - {data['rates'][currency]} {currency}" )
print(f"{data['base']} date-{data['date']}")
print()
rates = data['rates']
for curr in rates:
    print( f"{curr}: {rates[curr]}" )

di = {}
di[data['base']] = {}
print(di.get('EUR'))
for curr in rates:
    x = {curr: rates[curr]}
    di.update(x)
print(di['RUB'])
