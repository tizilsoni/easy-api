# pip install cuttpy
from cuttpy import Cuttpy

api_key = 'YOUR_API_KEY'
cuttly = Cuttpy(api_key)

resp = cuttly.shorten("Any website URL")
print(resp.shortened_url)