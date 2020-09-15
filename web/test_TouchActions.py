__author__ = 'zenghuan'

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver  import TouchActions



class Test_TouchActions:

    def setup(self):

        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()



    def teardown(self):
        self.driver.quit()

    def testScroll(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.XPATH,"//*[@id='kw']")
        ele_search = self.driver.find_element(By.XPATH,"//*[@id='su']")
        ele.send_keys("selenium test")
        action = TouchActions(self.driver)
        action.tap(ele_search).perform()
        action.scroll_from_element(ele,0,10000).perform()


