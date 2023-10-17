import requests
from lxml import etree

url = 'https://m.ip138.com/iplookup.php?from=baidu&ip=125.88.122.103'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
proxy = {
    'https': '61.227.209.48'
}

response = requests.get(url=url, headers=Headers, proxies=proxy).text
with open('./proxy.html', 'w', encoding='utf-8') as fp:
    fp.write(response)
