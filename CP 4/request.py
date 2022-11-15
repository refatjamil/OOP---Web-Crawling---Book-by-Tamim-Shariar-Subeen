import requests
url = "http://subeen.com/allposts"
response = requests.get(url)


print(type(response))


print(dir(response))

print(response.ok)


print(response.reason)