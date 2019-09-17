# -*- coding: utf-8 -*-
from selenium import webdriver
import time


#登录
def login():
    driver.find_element_by_id("x-URS-iframe")
    driver.switch_to.frame("x-URS-iframe")
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("liuping_lop")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("locuste123@")
    time.sleep(2)
    driver.find_element_by_id("dologin").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[class='u-btn u-btn-middle3 f-ib bgcolor f-fl']").click()
    time.sleep(10)
#退出
def logout():
    driver.find_element_by_link_text("退出").click()
    drvier.quit()

driver =webdriver.Edge()
driver.implicitly_wait(10)
driver.get("http://mail.163.com")
driver.implicitly_wait(5)
login()
driver.implicitly_wait(5)
#logout


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')


#s鼠标悬停至“搜索"连接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
time.sleep(5)

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

#接受告警框
driver.switch_to_alert().accept()

driver.quit()
