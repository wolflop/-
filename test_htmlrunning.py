# -*- coding: utf-8 -*-
import requests
import unittest
import HtmlTestRunner

class Logintest(unittest.TestCase):
    def setUp(self):
        self.url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    def testlogin1(self):
        form = {"mobilephone" : 13211111234, "pwd": "abc123"}
        r = requests.post(self.url, data=form)
        # print(r.text)
        self.assertEqual(r.text.split(), ['{"status":1,"code":"10001","data":null,"msg":"登录成功"}'])
    def testlogin2(self):
        form = {"mobilephone": "", "pwd": "abc123"}
        r = requests.post(self.url, data=form)
        # print(r.text.split())
        self.assertEqual(r.text.split(), ['{"status":1,"code":"20103","data":null,"msg":"手机号不能为空"}'])
def suite():
    loginTestCase = unittest.makeSuite(Logintest, "test")
    return loginTestCase

if __name__ == '__main__':
    fr = open(b'C://Users/liupi/projects/res3.html', "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream=fr, output="C://Users/liupi/projects/", report_title='test_report', descriptions="详情")
    runner.run(suite())
    fr.close()
