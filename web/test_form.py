__author__ = 'zenghuan'

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.XPATH,'//*[@id="user_login"] ').send_keys("529308803@qq.com")
        self.driver.find_element(By.XPATH,'//*[@id="user_password"]').send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR,'input.btn').click()
        sleep(2)
