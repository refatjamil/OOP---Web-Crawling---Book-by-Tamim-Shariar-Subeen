import requests

res = requests.get("http://dimikcomputing.com/abc/html")
print(res.ok)
print(res.reason)
print(res.status_code)