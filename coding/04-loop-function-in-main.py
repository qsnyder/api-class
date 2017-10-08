import json
import requests

accessToken = "NGQ2NGViYmEtYzdmNC00ZGIwLWE4ZTktZTkyYTJhMmQ4NGYzNDM5Y2EzZDAtNzhi" 


def setHeaders():         
	accessToken_hdr = 'Bearer ' + accessToken
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return spark_header


def getRooms(theHeader):    
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.get(uri, headers=theHeader)	
	return resp.json()
    

header=setHeaders()
value=getRooms(header)
print ("Spark Response Data:")
#print (json.dumps(value, indent=4, separators=(',', ': ')))
for data in value["items"]:	
	for room_info in data:
		key = room_info
		value = str(data[room_info])
		print(key + ":  " + value)
	print()
	print()
