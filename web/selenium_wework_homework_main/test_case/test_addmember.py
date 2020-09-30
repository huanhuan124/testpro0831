from web.selenium_wework_homework_main.page.main import Main

__author__ = 'zenghuan'

class Test_addmember:

    def setup(self):
        self.main = Main()


    def test_addmember(self):
        self.main.del_name()
        self.main.goto_addressList().goto_addmember().addmember()

    # def test_addmember2(self):
    #     self.main.goto_addmember()

