# Unittest

## Basic

### unittest

- test file must import unittest
- test class must inherent unittest.Testcase
- test function must start with test_

### pytest

- test file must start with test_ or end with _test
- test class name must start with Test
- test function must start with test_

## Fixtrues (Hooks)

### unitest

setUp/tearDown  在测试用例之前和之后执行

setUpClass/tearDownClass: Executing before or after, when testing the class.

setUpModule/teardownModule: Executing before or after, when testing the module.

### pytest

setup/teardown  在测试用例之前和之后执行

setup_class/teardown_class: Executing before or after, when testing the class.

setup_module/teardown_module: Executing before or after, when testing the module.

@pytest.fixtrue()



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

## Component

TestCase 测试用例：最小单元，业务逻辑。

TestSuite 测试套件：一组 TestCase 的集合，或者是TestSuite的集合，用来管理，打包多个 TestCase。

TestRunner 测试运行器：运行指定的 TestCase 或 TestSuite。

TestLoader 测试加载器：加载 TestCase 或 TestSuite，并且对  TestCase 和  TestSuite 功能的补充。

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

## unnittest 实例

unittest运行方式有两种

- 命令行的运行方式：

  1. `python3 -m unittest test_unitest.py`
  2. `python3 -m unittest test_unitest.TestUnittest.test_02_connect`
  3. `python3 -m unittest -v test_unitest.py`
  4. `python3 -m unittest -v test_unitest.py -k *_connect`

  -m：以脚本（命令行）的方式来运行测试用例

  -v：verbose 显示更详细

  -k：通过通配符*进行匹配方法名

- 通过main运行

  ```python
  if __name__ == "__main__":
      unittest.main()
  ```

## unittest 的测试用例运行结果

`.` 代表成功

`F` 代表失败

`E`代表错误

`s`代表跳过

不能通过用`-v`的方式运行， 因为`-v`是详尽的报错方式，不是简介的报错方式。

## unittest测试用例的执行顺序规则

以ASCII的编码的大小排序，【0-9, A-Z, a-z】

通过`print(ord('a'))` 查看ASCII码

## unittest的加载和运行测试用例的方式

**AddTest(测试类名('方法名'))**

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

**AddTests**

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

**加载一个目录下所有的测试用例**

```python
if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("./test", pattern="test_*.py")
    unittest.main(defaultTest="suite")
```

