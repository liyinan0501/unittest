import unittest

from test_01 import TestDemo1
from test_02 import TestDemo2

suite = unittest.TestSuite()
# suite.addTest(TestDemo1("test_method1"))
# suite.addTest(TestDemo1("test_method2"))
# suite.addTest(TestDemo2("test_method1"))
# suite.addTest(TestDemo2("test_method2"))

suite.addTest(unittest.makeSuite(TestDemo1))

runner = unittest.TextTestRunner()
runner.run(suite)
