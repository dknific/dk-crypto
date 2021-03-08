import requests
import config

apiURL = 'https://api.nomics.com/v1/currencies/ticker'
coins = ['BTC','ETH','DOGE','BNB','ADA','DOT','USDT','XRP','LTC','BCH','LINK']

def printOptions():
    print('Available cryptocurrencies:')
    print('----------------------------\n')
    for x in range(len(coins)):
        if (x % 2 != 0):
            print('       ' + coins[x] + '    ' + coins[x + 1])

def validateUserIn(userIn):
    if userIn.upper() in coins:
        return True
    else: return False

def getCurrencies(userIn):
    print('\nFetching value. Please wait...')
    print('...')
    response = requests.get(apiURL + '?key=' + config.API_KEY + '&ids=' + userIn)
    return response.json()

def roundValue(value):
    return "{:.{}f}".format(float(value),2)
