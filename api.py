import requests
api_key="BGARR4OFEG26I56P"
url =f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url)
print(response.json())
data= response.json()
print(type(data))
data2=data["Realtime Currency Exchange Rate"]
Exchange_rate=float(data2["5. Exchange Rate"])
print(Exchange_rate)