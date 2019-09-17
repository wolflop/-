# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest
import requests
from bs4 import BeautifulSoup

class Test1(unittest.TestCase):
    # def get_frame(self):
    #     url = "mail.163.com"
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #     response = requests.get(url, headers=headers)
    #     p = response.content.decode()
    #     bsobj = BeautifulSoup(p, 'html.parser')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("http://mail.163.com")
        self.driver.find_element_by_id("x-URS-iframe")
        self.driver.switch_to.frame("x-URS-iframe")
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("liuping_lop")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("locuste123@")
        time.sleep(2)
        self.driver.find_element_by_id("dologin").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("[class='u-btn u-btn-middle3 f-ib bgcolor f-fl']").click()
        time.sleep(10)
    def test_01(self):
        self.driver.find_element_by_id("_mail_component_24_24").click()

if __name__ == "__main__":
    unittest.main()
