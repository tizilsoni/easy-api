import json
import requests

api_key = "Your API Key"
api_url = "http://upload.giphy.com/v1/gifs"

param = {
   "q": "funny cat",
   "api_key": api_key,
   "limit": "10"
}

resp = requests.get(api_url, params=param)
data = json.loads(resp.text)
result = json.dumps(data, indent=4, sort_keys=True)
print(result)