import json
import requests

accessToken = ""


accessToken_hdr = 'Bearer ' + accessToken
spark_header = {'Authorization': accessToken_hdr}
uri = 'https://api.ciscospark.com/v1/rooms'
resp = requests.get(uri, headers=spark_header)

resp.text
resp.encoding
resp.headers

type(resp)
type(resp.json())

print (json.dumps(resp.json(), indent=4, separators=(',', ': ')))
