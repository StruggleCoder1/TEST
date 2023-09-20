url = 'https://baijiahao.baidu.com/s?id={}&for=pc'
id_list = ['1764613729907458053', '1764613729907458054']
for id in id_list:
    new_url = url.format(id)
    print(new_url)