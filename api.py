import requests

# Create a variable to store the api key
api_key="BGARR4OFEG26I56P"
# Create a variable to store the url
url =f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

# Get method to request access to the url and assign it as an object called "response"
response = requests.get(url)
# Retrieve data with .json from response and save it as data
data = response.json()
# Assign the exchange rate to the object "Exchange_rate"
Exchange_rate=float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

# Create a function called "exc" with a parameter "USD" to convert the USD to SGD
def exc(USD):
    """
    - This function is to convert USD to SGD
    - Input a number in the parameter to convert USD to SGD
    """

    # Do a converting by multiplying the exchange rate with the parameter input
    SGD=USD*Exchange_rate
    # Return SGD to the users
    return SGD
