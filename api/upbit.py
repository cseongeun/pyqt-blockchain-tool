import requests

class Upbit():
  def __init__(self):
    self.url = "https://api.upbit.com/v1/market/all?isDetails=false"
    self.headers = {"Accept": "application/json"}
    self.marketByCoin = {}

    self.getMarkets()

  def getMarkets(self):
    markets = requests.request("GET", self.url, headers=self.headers).json()

    for market in markets:
      marketName = market['market']

      if 'KRW' in marketName:
        targetCoin = marketName.replace('KRW-', '')

        self.marketByCoin[targetCoin] = marketName

    return self.marketByCoin


  def getCoins(self):
    return self.marketByCoin.keys()


if __name__ == '__main__':
  app = Upbit()
  ex = app.getMarkets()

  print(app.getCoins())
