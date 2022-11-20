import unittest

suite = unittest.TestLoader().discover("./case", pattern="test*.py")
unittest.TextTestRunner().run(suite)
