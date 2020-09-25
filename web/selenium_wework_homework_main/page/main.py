from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from web.selenium_wework_homework_main.page.addressbook import AddressBook
from web.selenium_wework_homework_main.page.base_page import BasePage


__author__ = 'zenghuan'



"""
20200925
改造：
1、封装公共部分-driver
2、封装公共部分-find_element_by
3、
"""
class Main(BasePage):
    # def __init__(self):
    #     #复用浏览器
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self._driver = webdriver.Chrome(options=options)
    #     self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

        #不复用浏览器
        # self._driver = webdriver.Chrome()
        # self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_addressList(self):
        #click addresslist
        sleep(2)
        #不知道怎么定位？？
        #点击通讯录按钮
        # self._driver.find_element_by_id("menu_contacts").click()
        # self._driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        self.find(By.ID,"menu_contacts").click()

        return AddressBook(self._driver)


    # def goto_addmember(self):
    #     self._driver.find_element_by_xpath("//div[contains(@class,'index_service')]").click()
    #     pass


