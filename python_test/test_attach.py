__author__ = 'zenghuan'
import allure
import pytest

def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一个HTML的body</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_jpg():
    allure.attach.file("D:/SoftwareInstall/pycharmworkspace/testpro0831/data/one.jpg",name="图片测试模块",attachment_type=allure.attachment_type.JPG)