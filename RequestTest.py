import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/116.0.0.0 Safari/537.36"}
result = [];
url="http://movie.douban.com/top250"
for start in range(0,250,25):
    parm = {
        'start':str(start)
    }
    response = requests.get(url,params=parm, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_titles = soup.findAll("a")
        for title in all_titles:
            all_links = title.findAll("span", attrs={"class": "title"})
            if '/' not in all_links:
                if all_links:
                    for link in all_links[0]:
                        print((str(link.text)))
                        result.append(link.text)
            else:
                print("请求失败")
with open('C:/Users/25064/Desktop/douban.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))
        # all_quote = soup.findAll("p", attrs={"class": "quote"})
        # for quote in all_quote:
        #     info = quote.findAll("span", attrs={"class": "inq"})
        #     print(info)


