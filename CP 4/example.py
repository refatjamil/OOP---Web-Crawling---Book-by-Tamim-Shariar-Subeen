import requests

res = requests.get("http://example.com")
print(res.ok)
print(res.text)
print(type(res.text))