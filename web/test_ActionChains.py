from selenium.webdriver import ActionChains

__author__ = 'zenghuan'


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys

class Test_ActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def testClick(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,"//input[@value='click me']")
        element_right_click = self.driver.find_element(By.XPATH,"//input[@value='right click me']")
        element_double_click = self.driver.find_element(By.XPATH,"//input[@value='dbl click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_double_click)
        action.perform()
        sleep(3)


    # 用link_text执行失败了，找不到设置？？？？
    def testMoveToElement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.XPATH,"//span[@id='s-usersetting-top']")
        # ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def testDragAndDrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.XPATH,"//*[@id='dragger']")
        ele_drop = self.driver.find_element(By.XPATH,"/html/body/div[2]")

        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag,ele_drop).perform()
        action.click_and_hold(ele_drag).release(ele_drop).perform()
        sleep(1)


    def testKeys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH,"/html/body/label[1]/input")

        action = ActionChains(self.driver)
        ele.click()
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(1)





