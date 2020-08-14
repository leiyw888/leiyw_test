
#! usr/bin/env python
# 百度demo
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 单元测试框架，使用该模块，我们可以对用例进行组织和运行，例如如下的BaiduTestCase类继承unittest.TestCase,该类执行会把test开头的方法当成一个测试用例去执行
import unittest


class BaiduTestCase(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例：')
        url = 'https://www.baidu.com'
        self.driver = webdriver.Chrome()  # 选择谷歌浏览器
        self.driver.get(url)  # 打开百度页面

    def test_bubutton(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('软件测试')  # 搜索框输入内容
        self.driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_id('kw').send_keys('博客园')
        self.driver.find_element_by_id('su').click()  # 点击百度按钮
        time.sleep(2)
        self.driver.save_screenshot('D:/baidu.png')  # 截图

    def tearDown(self):
        print('一条用例执行完成。')
        self.driver.quit()  # 退出浏览器


if __name__ == '__main__':
    unittest.main()