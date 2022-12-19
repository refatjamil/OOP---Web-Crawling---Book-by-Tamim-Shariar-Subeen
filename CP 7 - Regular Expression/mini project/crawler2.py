import re
import requests
import sys
import os

def creat_directory(name):
    print("Creating directory", name)
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name,"already exists")


def download_image(img_url, file_name):
    print("Downloading", img_url)
    r = requests.get(img_url)

    with open(file_name,'wb') as f:
        f.write(r.content)


def get_diractory_name(regex,url):
    result = re.findall(regex, url)
    dir_name = "_".join(result[0])
    return dir_name


# creat home directory 
main_dir = "dimik_pub2"
creat_directory(main_dir)
url = "http://dimik.pub"
response = requests.get(url)
if response.ok is False:
    sys.exit("Cloud not get response from server")

page_content = response.text
regex = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)</a>', re.S)   
result = re.findall(regex, page_content)
print(result)
dir_regex = re.compile(r'book/(\d+)/(\w+)-(\w+)-')

for item in result:
    name = item[2]
    url = item[0]
    img_url = item[1]

    dir_name = main_dir + "/" + get_diractory_name(dir_regex, url)
    creat_directory(dir_name)

    file_name = dir_name + "/" + "info.txt"
    with open(file_name, "w") as fp:
        fp.write(name + "\n")
        fp.write(url)

    img_file_name = dir_name + "/"  + "image.png"
    download_image(img_url, img_file_name)





