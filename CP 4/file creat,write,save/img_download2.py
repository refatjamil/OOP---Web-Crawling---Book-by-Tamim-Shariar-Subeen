import requests

img_url = "https://images.pexels.com/photos/60597/dahlia-red-blossom-bloom-60597.jpeg?cs=srgb&dl=pexels-pixabay-60597.jpg&fm=jpg&_gl=1*xknxcv*_ga*MTUxNjkxMzk3LjE2NjgyNzQzNzI.*_ga_8JE65Q40S6*MTY2ODI3NDM3NC4xLjEuMTY2ODI3NDYyNC4wLjAuMA.."

r = requests.get(img_url)

# print(r.content)
with open("flower.jpg","wb") as f:
    f.write(r.content)

