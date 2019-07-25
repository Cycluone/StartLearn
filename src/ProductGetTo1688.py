#!/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import os
import re
import time
import csv

savePath = "J:\\塑化产品\\yiwansuGo"

def get_Resource(url):
    """获取原始resource"""
    return requests.get(url)


def get_AddressData():
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
    """获取产品"""
    data = get_AddressData()

    for key in data.keys():
        if key == "HDPE-高密度聚乙烯":
            response = get_Resource(data[key])
            key = validateTitle(key)
            get_Data(response, key)





def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


def get_Data(response, ProdcutTypeName):
    soup = BS(response.content, 'html.parser')
    # print(soup)
    # 找是否有多页数据存在
    pages = soup.find("li", attrs={"class": "pagination"}).find_all("a")
    nextPage = False
    if len(pages)>= 2:
        # 删除上一页
        pages.pop(0)
        # 删除当前页 class = "current"
        pages.pop(0)
        # 删除下一页
        pages.pop(len(pages)-1)
        nextPage = True
    # print(len(pages))
    # print(pages)

    outPath = savePath + "\\" + ProdcutTypeName + "\\"
    try:
        if os.path.exists(outPath) != True:
            os.mkdir(outPath)
    except IOError:
        pass
    # out = open(outPath + ProdcutTypeName + ".csv", 'x', newline='')
    # csv_writer = csv.writer(out, dialect='excel')
    products = soup.find_all("li", attrs={"class": "offer-list-row-offer"})
    for product in products:
        a = product.find("a")
        price_container = product.find("em")
        csvData = [a['title'], price_container.get("data-highprice"), product.get("data-offerid")]
        image_item_summms = product.find_all("img", attrs={"class": "image-item-summm"})
        for image_item_summm in image_item_summms:
            url = "https:" + image_item_summm.get("data-bigsrc")
            url = url.replace("400x400", "800x800")
            url = url.replace("230x230", "800x800")
            imgFile = get_Image(url, outPath + "\\" + product.get("data-offerid") + "\\")
            print("======"+imgFile)
            csvData.append(imgFile)
        #csv_writer.writerow(csvData)
        # print(csvData)
    # 处理多界面数据
    if nextPage:
        for page in pages:
            url = page['href']
            response = get_Resource(url)
            soup = BS(response.content, "html.parser")
            products = soup.find_all("li", attrs={"class": "offer-list-row-offer"})
            for product in products:
                a = product.find("a")
                price_container = product.find("em")
                NextPageCsvData = [a['title'], price_container.get("data-highprice"), product.get("data-offerid")]
                image_item_summms = product.find_all("img", attrs={"class": "image-item-summm"})
                for image_item_summm in image_item_summms:
                    url = "https:"+image_item_summm.get("data-bigsrc")
                    url = url.replace("400x400", "800x800")
                    url = url.replace("230x230", "800x800")
                    imgFile = get_Image(url, outPath + "\\" + product.get("data-offerid") + "\\")
                    print("======"+imgFile)
                    NextPageCsvData.append(imgFile)
                #csv_writer.writerow(NextPageCsvData)
                # print(NextPageCsvData)


def get_Image(ImgUrl, saveUrl):

    if os.path.exists(saveUrl) == False:
        os.mkdir(saveUrl)
    filename = ""
    if ImgUrl != "":
        filename = os.path.basename(ImgUrl)
    else:
        filename = time.time() + ".jpg"

    r = get_Resource(ImgUrl)
    imgFile = saveUrl+filename
    file = open(imgFile, "wb")
    file.write(r.content)
    return imgFile


if __name__ == '__main__':
    getProduct()





# 查看响应头部字符编码
# print(response.encoding)


# https://cbu01.alicdn.com/img/ibank/2018/812/849/10220948218_288364205.400x400.jpg
# https://cbu01.alicdn.com/img/ibank/2018/812/849/10220948218_288364205.230x230.jpg
