# conding:utf-8
import requests
from bs4 import BeautifulSoup
import os

#打开acl
def parse_url():
    #获取爬虫页面
    url = "http://www.gaoqing.la"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    #返回抓取页面内容
    path1 = r"C:\Users\liupi\project"
    path = "gaoqing.html"
    file_path = os.path.join(path1, path)
    with open(file_path, "w", encoding='utf-8') as f:  # 保存当前页面.html
        f.write(response.content.decode())
    p = response.content.decode()
    bsobj = BeautifulSoup(p, 'html.parser')
    #抓取页面的电影的名字和连接
    namelist = bsobj.find_all("div", {"class": "article"})
    #抓取页面包含电海报连接
    posterlist = bsobj.find_all("div", {"class":"thumbnail"})
    getFilmName = []
    getFilmLink = []
    getFilmPoster = []
    for filmname in namelist:
         #获取当前页面的电影名字
        getFilmName.append(filmname.get_text().split()[1])
         #获取当前电影的连接
        getFilmLink.append(filmname.find('a').get('href'))
    #获取当前页面电影的连接
    for poster in posterlist:
        #获取当前页面电影的海报
        getFilmPoster.append(poster.find('img').get('src'))
    #获取当前页面每个电影的具体内容
    film_desc_content = []
    #遍历首页的所有连接
    for url_i in getFilmLink:
        response_i = requests.get(url_i, headers=headers)
        #获取每个连接的内容
        bsobj_i = BeautifulSoup(response_i.content.decode(), 'html.parser')
        #获取连接的信息
        film_descs = bsobj_i.find_all("div", {"class": "context"})
        for film_desc in film_descs:
            film_desc_content.append(film_desc.get_text())#将文字信息提取
    #将提取的信息保存成txt文件
    path2 = 'content.txt'
    file_path2 = os.path.join(path1, path2)
    with open(file_path2, "w", encoding='utf-8') as f:
        for i in film_desc_content:
            f.write(i)

if __name__ == '__main__':
    parse_url()
