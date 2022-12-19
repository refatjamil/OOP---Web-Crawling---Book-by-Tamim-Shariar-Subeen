import requests
import re

url = "https://books.toscrape.com/"

response = requests.get(url)
web_response =response.ok

text = response.text
category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(.*?)\s*<')
ll = category_pat.findall(text)
for i in ll:
    print('URLs  - ',i[0])
    print('Category Names - ',i[1])
    print('')