from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from web.selenium_wework_homework_main.page.addmember import AddMember

__author__ = 'zenghuan'

class AddressBook:
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def goto_addmember(self):
        #click add member
        #//*[@id="js_contacts58"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]
        sleep(5)
        #不知道怎么定位？？？
        #点击添加成员按钮
        self._driver.find_element(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_add_member:nth-child(2)').click()
        return AddMember(self._driver)