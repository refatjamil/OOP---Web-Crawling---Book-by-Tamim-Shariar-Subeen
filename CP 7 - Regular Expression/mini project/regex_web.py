import re
import requests
import sys
import os


# creat folder/directory
def creat_directory(name):

    try:
        os.makedirs(name)
    except FileExistsError:
        print(name,'alredy exists')


# images download function
def img_download(img_url_link):

    img_url = img_url_link                        # http img link
    pattern = re.compile(r'/\d{4}/\d{2}/(.+\.jpg|.+\.png)')
    img_name = pattern.findall(img_url)

    r = requests.get(img_url)
    with open(img_name[0],"wb") as f:
        f.write(r.content)



# first of all creat "dimik_pub" directory 
creat_directory("dimik_pub")


url = "http://dimik.pub"                           # website url link
response = requests.get(url)                       # get data from url
if response.ok is False:                           # check ulr response
    sys.exit("Clould not get response from server")
page_content = response.text                       # data convert to text(string)


# using regular expression
pattern = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)</a>',re.S)
data = re.findall(pattern,page_content)            # all data in data(data is type of list)


for item in data:
    
    # Name --> item[2]
    # URL --> item[0]
    # Image Url --> item[1]

    ree = re.compile(r'book/(\d+)/(\w+)-(\w+)',re.S)
    result = re.findall(ree,item[0])              # find book name from url item[0]
    book_name = "_".join(list(result[0]))


    path ="/home/rifat/Dev/Python/OOP & Web Crawling - Book by Tamim Shariar Subeen/CP 7 - Regular Expression/mini project/dimik_pub"  # path where make new folder/directory


    os.chdir(path)                               # change from current directory
    creat_directory(book_name)                   # creat new directory by book name using creat_directory method


    os.chdir(path + '/' + book_name)             # change path inside new book name directory
    img_download(item[1])                        # download image inside book name directory using img_download method


    # creat flie with info
    with open("info.txt","w") as f:
        f.write(f"Book Name: {item[2]}\n\nURL: {item[0]}\n\nImage URL: {item[1]}")

