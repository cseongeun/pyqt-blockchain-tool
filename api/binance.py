import requests

class Binance():
  def __init__(self):
    self.url = "https://api.binance.com/api/v3/exchangeInfo"
    self.headers = {"Accept": "application/json"}
    self.marketByCoin = {}

    self.getMarkets()

  def getMarkets(self):
    markets = requests.request("GET", self.url, headers=self.headers).json()
    markets = markets['symbols']

    for market in markets:
      if market['quoteAsset'] in ['BUSD','USDT']:
        self.marketByCoin[market['baseAsset']] = market['symbol']

    return self.marketByCoin

if __name__ == '__main__':
  app = Binance()
  ex = app.getMarkets()
  print(ex)

