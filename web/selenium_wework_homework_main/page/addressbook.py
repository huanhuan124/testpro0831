from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from web.selenium_wework_homework_main.page.addmember import AddMember
from web.selenium_wework_homework_main.page.base_page import BasePage

__author__ = 'zenghuan'

class AddressBook(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver = driver

    def goto_addmember(self):
        #click add member
        #//*[@id="js_contacts58"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]
        sleep(2)
        #不知道怎么定位？？？
        #点击添加成员按钮
        # self._driver.find_element(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_add_member:nth-child(2)').click()
        # self._driver.find_element_by_css_selector('.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)