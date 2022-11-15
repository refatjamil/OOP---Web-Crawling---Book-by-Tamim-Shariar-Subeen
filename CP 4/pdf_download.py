import requests
import sys

base_url = "http://subeen.com/downoad/"

info_dt = {"name":"Rifat","email":"rifatjamil54@gmail.com","country":"Bangladesh"}

url = base_url + "process.php"

print(url)

response = requests.post(url, data=info_dt)

if response.ok is False:
    sys.exit("Error downloading file")

with open("cpbook.pdf","wb") as fp:
    fp.write(response.content)

print("Book download complete!")        