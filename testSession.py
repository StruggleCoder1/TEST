from selenium.webdriver.support import expected_conditions as EC

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

bro = webdriver.Chrome()
bro.get('http://www.baidu.com')
page_context = bro.page_source
search_input = bro.find_element(By.ID, 'kw')
search_input.send_keys("美女")
search_click = bro.find_element(By.ID, 'su')
search_click.click()
# # 等待目标元素加载完成
# selenium跳转之后的页面也可以直接获取相关元素
# search_input_new = bro.find_element(By.XPATH, '//*[@id="1"]/div/section/div[2]/div[2]/div/section[1]/div/div[2]/a')
# search_input_new.click()
# print(search_input_new.get_attribute('title'),"111")
# print(search_input_new.get_attribute('href'),"111")
url = 'https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=b71381b00000256b&wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xd3ea1c050000b568&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=%25E7%25BE%258E%25E5%25A5%25B3&rsv_btype=t&rsv_t=806diCZQ%2FMDDM4LsKXNz7wHHk%2FxDKDjgEwb9ZlavEA7YOMWDmyg8tmDCo0uqyTZCwUiv&rsv_pq=b71381b00000256b&rsv_sug3=9&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=5&rsv_sug4=3779&rsv_sug=1&bs=%E7%BE%8E%E5%A5%B3&rsv_sid=39320_39363_39390_39347_39407_39097_39415_39437_39358_39307_39233_39404_26350_39423&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=44466'
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
params = {
    'ie': 'utf-8',
    'wd': '美女',
    'bs': '美女'
}
response = requests.get(url=url, headers=Headers, params=params).text
with open('./baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response)
tree = etree.HTML(response)
a = tree.xpath('//td[@class="rs-col_8Qlx-"]/a/@title')
print(a)

sleep(3)
bro.quit()
