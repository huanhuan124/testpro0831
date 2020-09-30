from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from web.selenium_wework_homework_main.page.base_page import BasePage

__author__ = 'zenghuan'

class AddMember(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self._driver = driver

    def addmember(self):
        # self._driver.implicitly_wait(1)
        self.find(By.ID,'username').send_keys("acs")
        self.find(By.ID,'memberAdd_acctid').send_keys('a120')
        self.find(By.ID,'memberAdd_phone').send_keys('13045678954')
        # self._driver.find_element_by_id('username').send_keys("acs")
        # self._driver.find_element_by_id('memberAdd_acctid').send_keys('a120')
        # self._driver.find_element_by_id('memberAdd_phone').send_keys('13045678954')

        #不知道怎么定位
        #点击保存按钮
        #这种xpath的方式第二天就不能用了，不知道为什么
        # self._driver.find_element_by_xpath('//*[@id="js_contacts58"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        #通过css_selector
        # self._driver.find_element_by_css_selector('.qui_btn.ww_btn.js_btn_save:nth-child(2)').click()
        self.find(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save:nth-child(2)').click()
        #通过xpath
        # self._driver.find_element_by_xpath('//div[@class="member_edit"]//div[3]//a[2]').click()
        # sleep(2)
        self._driver.quit()
