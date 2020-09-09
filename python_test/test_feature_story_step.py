__author__ = 'zenghuan'
import pytest
import allure

class TestAllure():

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("http://www.baidu.com",name="链接")
    def test_login_sucess(self):
        print("登陆成功")

    TEST_CASE_LINK = "http://www.weibo.com"
    @allure.testcase(TEST_CASE_LINK,"登陆用例")
    def test_with_case_link(self):
        print("这是一条测试用例的链接，链接到测试用例里面")

    #运行程序时需要加上   --allure-link-pattern=issue:http://mytesttracker.com/issue/{}
    @allure.issue("140","这是一个bug链接")
    def test_with_issue_link(self):
        print("bug链接")



    def test_login_fail(self):
        print("登陆失败")

    def test_login_userfail(self):
        print("用户名缺失")

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_passfail(self):
        print("密码缺失")

        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        print("点击登陆")

        with allure.step("点击登陆后失败"):
            assert '1' == 1
            print("点击登陆后失败")
