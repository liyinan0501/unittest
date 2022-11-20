# Basic

- test file must import unittest
- test class must inherent unittest.Testcase
- test function must start with test\_

断言：

unittest: self.assertEqual() self.assertin()

pytest: pythoin asseet

报告：

unittest: HtmlTestrunner.py

pytest: pytest-html.allure

失败重跑：

unittest: no

pytest: pytest-rerunfailures

参数化：

unittest: ddt

pytest: @pytest.mark.parametrize()

# Component

TestCase 测试用例：最小单元，业务逻辑。

TestSuite 测试套件：一组 TestCase 的集合，或者是 TestSuite 的集合，用来管理，打包多个 TestCase。

TestRunner 测试运行器：运行指定的 TestCase 或 TestSuite。

TestLoader 测试加载器：加载 TestCase 或 TestSuite，并且对 TestCase 和 TestSuite 功能的补充。

TestFixture 测试夹具：书写在 TestCase 代码中，是一种代码结构，可以在每个方法执行前后执行的内容。

## 测试代码

```python
class TestUnittest(unittest.TestCase):
    def test_01_discover(self):
        print("start to test discover")

    def test_02_connect(self):
        print("start to test connect")

    def test_03_notify(self):
        print("start to test notify")
```

# unnittest 实例

unittest 运行方式有两种

- 命令行的运行方式：

  1. `python3 -m unittest test_unitest.py`
  2. `python3 -m unittest test_unitest.TestUnittest.test_02_connect`
  3. `python3 -m unittest -v test_unitest.py`
  4. `python3 -m unittest -v test_unitest.py -k *_connect`

  -m：以脚本（命令行）的方式来运行测试用例

  -v：verbose 显示更详细

  -k：通过通配符\*进行匹配方法名

- 通过 main 运行

  ```python
  if __name__ == "__main__":
      unittest.main()
  ```

# unittest 的测试用例运行结果

`.` 代表成功

`F` 代表失败

`E`代表错误

`s`代表跳过

不能通过用`-v`的方式运行， 因为`-v`是详尽的报错方式，不是简介的报错方式。

# unittest 测试用例的执行顺序规则

以 ASCII 的编码的大小排序，【0-9, A-Z, a-z】

通过`print(ord('a'))` 查看 ASCII 码

# unittest 的加载和运行测试用例的方式

## AddTest

```python
if __name__ == "__main__":
    # create a testing suite
    suite = unittest.TestSuite()
    # option 1: add specific functions need to test via suite
    suite.addTest(TestUnittest("test_01_discover"))
    suite.addTest(TestUnittest("test_03_notify"))
    # option 2: add the all functions from the class need to test via suite
    suit.addTest(unittest.makeSuite(TestUnittest))
    # run suite
    unittest.main(defaultTest="suite")
```

## **AddTests**

```python
if __name__ == "__main__":
    # create a testing suite
    suite = unittest.TestSuite()
    # add testing instances via suite.addTests
    testcases = [TestUnittest("test_01_discover"), TestUnittest("test_03_notify")]
    suite.addTests(testcases)
    # run suite
    unittest.main(defaultTest="suite")
```

## **TestLoader**

和 TestSuite 的作用一样，对 TestSuite 功能的补充，用来组装测试用例的，加载一个目录下所有的测试用例。

```python
import unittest

suite = unttest.TestLoader().discover("./case", pattern="test*.py")
# suite = unittest.defaultTestLoader.discover("./case", pattern="test*.py")
unittest.TextTestRunner().run(suite)
```

# Fixtrues (Hooks)

是一种代码结构，在某些特定情况下，会自动执行。

## Function Level

在每个测试方法，执行前后都会自动调用的结构。

```python
# 方法之前执行
def setUp(self):

# 之间为测试用例

# 方法执行之后
def tearDown(self):
```

## Class Level

在每个测试类中所有方法执行前后，都会自动调用的结构（在整个类中，执行之前之后只执行一次）。

```python
# 类中所有方法之前
@classmethod
def setUpClass(cls):

# 类中所有方法之后
@classmethod
def tearDownClass(cls):
```

## Module Level

模块：代码文件

在每个代码文件执行前后执行的代码结构。

```python
# 模块级别的需要写在类的外边直接定义函数即可
# 代码文件之前
def setUpModule():

# 代码文件之后
def tearDownModule():
```
