import unittest
from tools import add


class TestAdd(unittest.TestCase):
    def test_01(self):
        if add(1, 2) == 3:
            print("Test succeeds")
        else:
            print("Test fails")

    def test_02(self):
        if add(10, 20) == 30:
            print("Test succeeds")
        else:
            print("Test fails")

    def test_03(self):
        if add(2, 3) == 5:
            print("Test succeeds")
        else:
            print("Test fails")
