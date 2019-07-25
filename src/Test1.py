#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os
# print(os.path.exists("J:\\塑化产品\\yiwansu\\ABS"))




url = "https://yiwansu.1688.com/page/offerlist_94719354.htm?spm=a2615.7691456.autotrace-paginator.3.36623f9anCWSAP&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=wangpu_score&pageNum=2#search-bar"
import requests
from bs4 import BeautifulSoup as BS
import os
import re
import time
import csv

