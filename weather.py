import requests

api_key = "Your API Key"
url = "https://api.m3o.com/v1/weather/Forecast"
params = {"days":"2", "location":"India"}

headers = {
'Content-Type': "application/json", 
'Authorization': "Bearer "+ api_key
}

response = requests.request("GET", url, headers=headers, params=params)
print (response.json)