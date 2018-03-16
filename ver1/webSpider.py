import urllib2
from bs4 import BeautifulSoup




class Scrap:

  def __init__(self, url):
    self.url = url
    self.request = urllib2.Request(self.url);
    self.response = urllib2.urlopen( self.request )
    self.html = self.response.read();
    self.soup = BeautifulSoup(self.html, "html.parser")

  def getSingle(self):

    testTag = self.soup.find_all("span", {"id": "quote_price"})
    OverallVal = "1 BTC => "

    for tag in testTag:
      specificVal = tag.find_all("span")
      for tag in specificVal:
       OverallVal+= " " + tag.text

    return OverallVal

  def getMarketValue(self):
      MarkCapDiv = self.soup.find("div", {"class": "coin-summary-item-detail details-text-medium"})
      MarkCapValues = MarkCapDiv.find_all("span")
      return "Market Cap " + MarkCapValues[3].text.strip() + " => " + MarkCapValues[1].text + " " + MarkCapValues[2].text

  def getVolume24hr(self):
    VolumeDiv = self.soup.find_all("div", {"class": "coin-summary-item"})[1]
    return VolumeDiv.find("h3").text + " " + VolumeDiv.find_all("span")[0].text + " BTC: " + VolumeDiv.find_all("span")[4].text



print(Scrap('https://coinmarketcap.com/currencies/bitcoin/').getVolume24hr())


def scrape(url):

  request = urllib2.Request(url);
  response = urllib2.urlopen( request )
  html = response.read();
  soup = BeautifulSoup(html, "html.parser")
  testTag = soup.find_all("span", {"id": "quote_price"})
  OverallVal = "1 BTC => "
  for tag in testTag:
    specificVal = tag.find_all("span")
    for tag in specificVal:
     OverallVal+= " " + tag.text

  print(OverallVal)

  #market cap
  MarkCapDiv = soup.find("div", {"class": "coin-summary-item-detail details-text-medium"})
  MarkCapValues = MarkCapDiv.find_all("span")
  print("-")*30
  print("Market Cap")
  print("")
  print(MarkCapValues[3].text.strip() + " => " + MarkCapValues[1].text + " " + MarkCapValues[2].text)
  print("-")*30



scrape('https://coinmarketcap.com/currencies/bitcoin/');