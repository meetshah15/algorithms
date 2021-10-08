import requests

url = "https://www.colourlovers.com/api/colors/random"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
