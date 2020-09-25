from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from web.selenium_wework_homework_main.page.addressbook import AddressBook


__author__ = 'zenghuan'

class Main:
    def __init__(self):
        #复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

        #不复用浏览器
        # self._driver = webdriver.Chrome()
        # self._driver.get('https://work.weixin.qq.com/wework_admin/frame')


    def goto_addressList(self):
        #click addresslist
        sleep(2)
        # elements = self._driver.find_elements_by_css_selector(".frame_nav_item_title")
        # for elment in elements:
        #     print(elment.get_attribute())
        #不知道怎么定位？？
        #点击通讯录按钮
        self._driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()


        return AddressBook(self._driver)


    def goto_addmember(self):
        self._driver.find_element_by_xpath()


