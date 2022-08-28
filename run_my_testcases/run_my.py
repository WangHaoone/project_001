import unittest

from my_test_cases.testLonginPage import TestLoginPage
from run_my_testcases.HTMLTestRunnerX import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginPage))
    file = open(file='../reports/测试报告.html',mode='wb')
    runner = HTMLTestRunner(stream=file,verbosity=3,title='自动化测试报告')
    runner.run(suite)