import requests
import sys

img_url = sys.argv[1]  # img_url = http://goo.gl/Q7LmXw
file_name = sys.argv[2] # file_name = ccc.png

response = requests.get(img_url) # response = requests.get(http://goo.gl/Q7LmXw) 

with open(file_name,"wb") as f: # f = ccc.png
    f.write(response.content)