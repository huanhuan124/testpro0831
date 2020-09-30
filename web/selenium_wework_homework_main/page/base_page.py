from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

__author__ = 'zenghuan'
class BasePage:
        _driver = None
        _base_url = ""
        def __init__(self,driver:WebDriver = None):
        #复用浏览器

            if self._driver is None:
                options = Options()
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                self._driver = driver
            # self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
            print(self._base_url+"*********************")
            if self._base_url != "":
                self._driver.get(self._base_url)


        def find(self,by,locator):
            return self._driver.find_element(by,locator)