import json
import urllib.request, urllib.parse, urllib.error


serviceurl = "http://py4e-data.dr-chuck.net/json?s"
data_address = "Indiana University at Bloomington"
address_wanted = data_address


parameters = {"address": address_wanted}
paramsurl = urllib.parse.urlencode(parameters)

queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

data = urllib.request.urlopen(queryurl).read()


jsdata = json.loads(data)
place_id = jsdata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
