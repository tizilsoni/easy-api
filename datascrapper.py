import requests as req 
api_key = "YOUR_API_KEY"
web_url = "https://www.amazon.com/" #or any other url

param = {
  'access_key': api_key,
  'url': web_url
}

resp = req.get('http://api.scrapestack.com/scrape', param)
website_data = resp.content
print(website_data)