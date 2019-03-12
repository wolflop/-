# -*- coding: utf-8 -*-
import requests
import os
import re
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup

class Tieba:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        # self.headers = {'User-Agent': " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
    def get_url_list(self):
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in  range(1000)]
    def parse_url(self, url):  #发送请求，获取响应
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):   #保存html字符串
        path1 = "C:\\Users\\liupi\\project"
        path = "{}-第{}页.html".format(self.tieba_name, page_num)
        file_path = os.path.join(path1, path)
        with open(file_path, "w", encoding='utf-8') as f:        #李毅第几页.html
            f.write(html_str)
    def run(self):  #实现主逻辑
        #构造url列表
        url_list = self.get_url_list()
        #遍历发送请求响应
        for url in url_list:
            html_str = self.parse_url(url)
            #保存
            page_num =  url_list.index(url) + 1 #页码数
            self.save_html(html_str, page_num)


class Baike:
    def __init__(self, search_for):
        self.search_for = search_for
        self.url_temp = "https://baike.baidu.com/item/"+search_for+""
    def parse_url(self, url):  #发送请求，获取响应
        # print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return  response.content.decode()
    def save_html(self, html_str):   #保存html字符串
        path1 = r"C:\Users\liupi\project"
        path = "{}.html".format(self.search_for)
        file_path = os.path.join(path1, path)
        with open(file_path, "w", encoding='utf-8') as f:        #搜索页面.html
            f.write(html_str)
    def run(self):  # 实现主逻辑
        html_str = self.parse_url(self.url_temp)
        # print(self.url_temp)
        self.save_html(html_str)   # 保存
    def find_str(self):
        # print(self.url_temp)
        p = self.parse_url(self.url_temp)
        bsobj = BeautifulSoup(p, 'html.parser')
        # a = bsobj.head.find_all("meta")[3]
        b = re.findall('[\u4e00-\u9fa5]+', str(bsobj.head.find_all("meta")[3]))
        path1 = r"C:\Users\liupi\project"
        path = "{}.txt".format(self.search_for)
        file_path = os.path.join(path1, path)
        with open(file_path, "w", encoding='utf-8') as f:
            for i in range(len(b)):
                f.write(b[i])
        # print(b)
        # des = bsbj.head.contents[3].split('\n')

        # p = re.findall('<div class="para" label-module="para">(.*?)</div>', p, re.S)
        # p = re.findall('[\u4e00-\u9fa5]+', p, re.S)
        # for i in range(len(p)):
        #     p1 = re.findall('[\u4e00-\u9fa5]+', p[i], re.S)
        # for  child in bsobj.head.descendants:
        #     print(type(child{0}))
        # path1 = r"C:\Users\liupi\project"
        # path = "{}.txt".format(self.search_for)
        # file_path = os.path.join(path1, path)
        # with open(file_path, "w", encoding='utf-8')     as f:
        #     for i in range(len(p)):
        #         f.write(p[i])
            # print(p1[0])
    # def hebing(self, str):



if __name__ == '__main__':
    tieba_spider = Baike("lol")
    tieba_spider.run()
    tieba_spider.find_str()