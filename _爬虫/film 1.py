import requests
from  lxml import etree
from time import sleep

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}

# hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
# hero_list_resp = requests.get(hero_list_url,headers=headers)
# for h in hero_list_resp.json():
#     ename = h.get('ename')

    # for i,n in enumerate(ename):
resp = requests.get(f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/155/155.jpg')
#接收服务器响应的图片（皮肤）
#保存图片（皮肤）
with open('155.jpg','wb') as f:
    f.write(resp.content)
print(f'已下载皮肤')
sleep(0.01)
    



https://game.gtimg.cn/images/yxzj/img201606/heroimg/155/155.jpg