import time

from common.selenium_driver import logger


class PageObject:

    def __init__(self,driver):
        self.driver = driver
    #c查找元素..find_element(By.xxx,'value')
    def getElement(self,*args):

        return self.driver.find_element(*args)

    #查找多个元素
    def getElements(self,*args):
        return self.driver.find_elements(*args)

    #打开网页
    def open(self,url):
        self.driver.get(url)

     #截图
    def screen_shop(self,title):
        logger.info('即将截图:'+str(title))
        #../screen_shots/登录失败_20210517090909.png
        t = time.strftime('%Y%m%d%H%M%S',time.localtime())
        path = '../screen_shots/'+str(title)+'_'+str(t)+'png'
        self.driver.get_screenshot_as_file(path)