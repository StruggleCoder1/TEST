import requests
from lxml import etree
import os
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = 'https://sc.chinaz.com/jianli/'
    for i in range(1,1208):
        current_url = url+'/index_'+str(i)+'.html'
        print(current_url)
        response = requests.get(url=current_url, headers=headers).text
        tree = etree.HTML(response)
        all_data_div = tree.xpath('//div[@class="sc_warp  mt20"]/div/div')
        if not os.path.exists ('./rar_data'):
            os.mkdir('./rar_data')
        for i in all_data_div:
            target_path = i.xpath('./div/a/@href')
            for j in target_path:
                response = requests.get(url=j, headers=headers)
                response.encoding='utf-8'
                inner_tree = etree.HTML(response.text)
                down_path = inner_tree.xpath('//ul[@class="clearfix"]/li')[0]
                end_down_path = down_path.xpath('./a/@href')[0]
                name =inner_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
                # name = name.encode('iso-8859-1').decode('gbk')
                # print(name)
                response = requests.get(url=end_down_path, headers=headers).content
                with open('./rar_data/'+name,'wb') as  f:
                    f.write(response)
                    # print('下载'+name+'成功')
