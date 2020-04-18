import requests

r = requests.get('https://poloniex.com/public?command=returnTicker')

cripto = r.json()

for i in cripto.items():
    print(i[0], ':', i[1]['last'])

