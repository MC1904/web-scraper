import requests

url = ""
page = requests.get(url)
print(page.text)
