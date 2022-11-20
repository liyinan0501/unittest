import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("input http address.")

    def tearDown(self):
        print("close current page.")

    @classmethod
    def setUpClass(cls):
        print("open browser")

    @classmethod
    def tearDownClass(cls):
        print("close browser")

    def test_1(self):
        print("input correct username and password, and click login.")

    def test_2(self):
        print("input wrong username and password, and click login.")
