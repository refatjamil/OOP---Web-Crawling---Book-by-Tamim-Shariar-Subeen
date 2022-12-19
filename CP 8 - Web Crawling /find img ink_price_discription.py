import re
import requests

url = "https://books.toscrape.com/catalogue/the-exiled_247/index.html"
response = requests.get(url)
html_text = response.text

img_link_pattern = re.compile(r' <div class="item active">\s*<img src="(.*?)"')
img_link = img_link_pattern.findall(html_text)
print("Image Link: "+img_link[0])
print('')

product_discription_pattern = re.compile(r'<div id="(.*?)" class="sub-header">\s*<h2>Product Description</h2>\s*</div>\s*<p>\s*(.*?)\s*</p>')
product_discription = product_discription_pattern.findall(html_text)
print((product_discription[0][0]).replace('_',' ').upper()+': '+product_discription[0][1])
print('')

product_info_paattern = re.compile(r'<th>(.*?)</th>\s*<td>(.*?)</td>')
product_info = product_info_paattern.findall(html_text)
for j in [i[0]+': '+i[1] for i in product_info]:
    print(j)


# img_link_pattern = r'<div class="item active">\s*<img src="(.*?)"'
# product_discription_pattern = r'<div id="(.*?)" class="sub-header">\s*<h2>Product Description</h2>\s*</div>\s*<p>\s*(.*?)\s*</p>'
# product_info_paattern = r'<th>(.*?)</th>\s*<td>(.*?)</td>'

# pattern = [img_link_pattern,product_discription_pattern,product_info_paattern]

# for i in pattern:
#     result = re.findall(i,html_text)
#     print(result.__len__())