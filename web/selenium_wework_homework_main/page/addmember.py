from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver

__author__ = 'zenghuan'

class AddMember:

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def addmember(self):
        sleep(2)
        self._driver.find_element_by_id('username').send_keys("acs")
        self._driver.find_element_by_id('memberAdd_acctid').send_keys('a120')
        self._driver.find_element_by_id('memberAdd_phone').send_keys('13045678954')

        #不知道怎么定位
        self._driver.find_element_by_xpath('//*[@id="js_contacts58"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        sleep(2)
        self._driver.quit()
