import urllib2
from bs4 import BeautifulSoup
import re
import datetime
import time

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

    string = """
    Single Value
    ---------------
    {value}
    ---------------

    """


    # return string.format(value = OverallVal)
    return string.format(value = OverallVal)

  def getMarketValue(self):
    MarkCapDiv = self.soup.find("div", {"class": "coin-summary-item-detail details-text-medium"})
    MarkCapValues = MarkCapDiv.find_all("span")
    USDvalue = MarkCapValues[1].text + " " + MarkCapValues[2].text
    BTCvalue = re.findall(r'\d+(?:,\d+)?',  MarkCapValues[3].text.strip())
    string = """
    Market Cap
    ---------------
    ${USD} => BTC{BTC}
    ---------------
    """

    return string.format(USD = USDvalue, BTC = BTCvalue)



  def getVolume24hr(self):
    VolumeDiv = self.soup.find_all("div", {"class": "coin-summary-item"})[1]
    print( VolumeDiv.find_all("span")[4].text.split(" "))
    btcPrice = re.findall(r'\d+(?:,\d+)?', VolumeDiv.find_all("span")[4].text)
    string = """
    {title} 
    ---------------
    {USD} => {BTC}BTC
    ---------------

    """

    return string.format(title = VolumeDiv.find("h3").text, USD= "$" + VolumeDiv.find_all("span")[1].text, BTC=btcPrice)

  def getAll(self):
    sin =self.getSingle()
    mv = self.getMarketValue()
    v24 = self.getVolume24hr()
    time = datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S")
    btcTXTFILE = open("bitcoin.txt", "w")
    btcTXTFILE.write(time + sin + mv + v24)
    btcTXTFILE.close()


def scuffedCronJob():
    Scrap('https://coinmarketcap.com/currencies/bitcoin/').getAll()


while True:
    scuffedCronJob()
    print("refreshed")
    time.sleep(2) # wait one minute

'''
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

'''