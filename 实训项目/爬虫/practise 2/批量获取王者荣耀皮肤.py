#1.发送请求
#发送请求的模块（为第三方库，需要在外部安装） pip install requests
import requests 
#解析html代码的工具
from lxml import etree
import os
from time import sleep

#伪装自己
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}    
#获取英雄列表
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url,headers=headers)
print(hero_list_resp.json())
for h in hero_list_resp.json():
    ename = h.get('ename')
    cname = h.get('cname')

    if not os.path.exists(cname):
        os.makedirs(cname)
    
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url,headers=headers)
    hero_info_resp.encoding = 'gbk'
    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = [name[0:name.index('&')] for name in names.split('|')]
      

    #发送请求
    for i,n in enumerate(names):
        resp = requests.get(f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg')
        #接收服务器响应的图片（皮肤）
        #保存图片（皮肤）
        with open(f'{cname}/{n}.jpg','wb') as f:
            f.write(resp.content)
        print(f'已下载:{n}的皮肤')
        sleep(1)
        

