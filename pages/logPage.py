from time import sleep

from common.selenium_driver import logger
from selenium.webdriver.common.by import By

from data.urlPath import LOGIN_URL
from pageObject.pageObject import PageObject
#
# 0. 每个页面都要继承PageObject
class LoginPage(PageObject):

#1. 记录需要的元素...格式固定
    nameInput = (By.ID,"username")
    pwdInput = (By.NAME,'password')
    loginButton = (By.CLASS_NAME,'submit')

#2. 编写操作函数
    def login(self,name,pwd):
        #打开登录页面
        logger.info('即将打开登录页面')
        self.open(LOGIN_URL)

        logger.info('输入用户名:'+str(name))
        self.getElement(*self.nameInput).clear()
        self.getElement(*self.nameInput).send_keys(name)

        #输入密码
        logger.info('输入密码:' + str(pwd))
        self.getElement(*self.pwdInput).clear()
        self.getElement(*self.pwdInput).send_keys(pwd)

        #点击登录按钮
        self.getElement(*self.loginButton).click()
        sleep(2)
    #3.检查操作后状态函数
    def checklogin(self):
        if self.driver.title == '会员登录':
            #登录失败
            logger.info('登录失败,去截图')
            self.screen_shop('登录失败')
            return False
        else:
            logger.info('登录成功,去截图')
            self.screen_shop('登录成功')
            return True