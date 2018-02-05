import urllib2
import json

MACaddr = "BC:92:6B:A0:00:01"
url = "http://macvendors.co/api/"

request = urllib2.Request(url+MACaddr, headers={'User-Agent' : "API Browser"}) 


response = urllib2.urlopen( request )

obj = json.load(response)

print (obj['result']['company']);


