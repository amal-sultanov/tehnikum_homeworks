import requests

# link = 'https://icanhazip.com'
# print(requests.get(link).text)

data = {
    "comments": "feqwfrq",
    "custemail": "vaf@ffwr.frq",
    "custname": "sdvsfv",
    "custtel": "vfsv",
    "delivery": "",
    "size": "medium",
    "topping": "mushroom"
}

url = 'https://httpbin.org/post'
print(requests.post(url, data=data))
