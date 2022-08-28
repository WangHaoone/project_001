import unittest

import ddt
from common.myUnit import MyUnit
from common.selenium_driver import getCsvData

from pages.logPage import LoginPage


result = getCsvData('../data/login.csv')
list = []
for r in result:
    dict = {'name':r[0],'pwd':r[1],'yq':r[2]}
    list.append(dict)

@ddt.ddt
class TestLoginPage(MyUnit):
    @ddt.data(*list)
    def test_login(self,ls):
        lp = LoginPage(self.driver)
        lp.login(ls['name'], ls['pwd'])

        if ls['yq'] == '成功':
            self.assertEqual(lp.checklogin(),True)
        else:
            self.assertEqual(lp.checklogin(),False)

if __name__ == '__main__':
    unittest.main()
