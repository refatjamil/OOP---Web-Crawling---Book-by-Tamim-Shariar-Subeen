import re, requests


url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

i = url.rfind("/")
print(i)
url2 = url[0:i+1]+"page-2.html"


response = requests.get(url)
response2 = requests.get(url2)


text = response.text
text2 = response2.text



pattern = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
result = pattern.findall(text)
result2 = pattern.findall(text2)



# for i in result:
#     print('url: ',i[0])
#     print('book name: ',i[1])
#     print('')

# for i in result2:
#     print('url: ',i[0])
#     print('book name: ',i[1])
#     print('') 

