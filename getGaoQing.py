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
    # print(type(namelist))
    #获取当前页面的电影名字
    getFilmName = []
    for filmname in namelist:
        getFilmName.append(filmname.get_text().split()[1])
    #获取当前页面电影的连接
    getFilmLink = []
    for filmlink in namelist:
        # if 'href' in filmlink.findall("a"):
        print(filmlink.find_all("a"))
        # getFilmLink.append()
    # print(getFilmLink)

if __name__ == '__main__':
    parse_url()
