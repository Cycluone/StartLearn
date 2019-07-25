#!/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import os
import sys
import time
def get_Resource(url):
    """获取原始resource"""
    return requests.get(url)

def get_Data():
    """获取塑料类型及链接地址"""
    plactis = {}
    response = get_Resource("https://yiwansu.1688.com/")
    soup = BS(response.content, 'html.parser')
    data = soup.find("div", attrs={'class': 'bd'})
    alist = BS(str(data), 'html.parser').find_all("a")
    for a in alist:
        plactis[a['title']] = a['href']
    return plactis


def getProduct():
    data = get_Data()
    for key in data.keys():
        response = get_Resource(data[key])
        get_Data1(response)

def get_Data1(response):
    soup = BS(response.content, 'html.parser')
    products = soup.find_all("li", attrs={"class": "offer-list-row-offer"})
    for product in products:
        a = product.find("a")
        image_item_summms = product.find_all("img", attrs={"class": "image-item-summm"})
        for image_item_summm in image_item_summms:
            url = "https:"+image_item_summm.get("data-bigsrc")
            url = url.replace("400x400", "800x800")
            url = url.replace("230x230", "800x800")
            get_Image(url)
            sys.exit(0)
        # print(a['title'])
        # print(product.get("data-offerid"))


def get_Image(url):
    filename = ""
    if url != "":
        filename = os.path.basename(url)
    else:
        filename = time.time() + ".jpg"

    r = get_Resource(url)
    file = open(filename, "wb")
    file.write(r.content)


if __name__ == '__main__':
    getProduct()





# 查看响应头部字符编码
# print(response.encoding)


# https://cbu01.alicdn.com/img/ibank/2018/812/849/10220948218_288364205.400x400.jpg
# https://cbu01.alicdn.com/img/ibank/2018/812/849/10220948218_288364205.230x230.jpg
