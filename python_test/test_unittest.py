__author__ = 'zenghuan'

import unittest


class demo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("demo1 setupcalss")

    @classmethod
    def tearDownClass(cls):
        print("demo1 teardownclass")

    def setUp(self):
        print("demo1 setup")

    def tearDown(self):
        print("demo1 teardown")

    def test_case1(self):
        print("demo1 testcase1")

    def test_case2(self):
        print("demo1 testcase2")


class demo2(unittest.TestCase):
    def test_case1(self):
        print("demo2 testcase1")

    def test_case2(self):
        print("demo2 testcase2")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(demo1.test_case1)
    suite.addTest(demo1("test_case1"))
    suite.addTest(demo1("test_case2"))
    suite.addTest(demo2.test_case1)
    unittest.TextTestRunner().run(suite)
