import csv
import logging
from logging import config

from selenium import webdriver

#从配置文件中配置日志
config.fileConfig('../config/log.conf')
#获取日志打印对象.....以后打印日志的时候  只需要调用logger对象就可以
logger = logging.getLogger()
#创建函数..获取驱动对象
def selenium_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)

    return driver

def getCsvData(csv_file):
    file = open(file=csv_file,mode='r',encoding='utf-8-sig')
    result = csv.reader(file)
    return result

if __name__ == '__main__':
    # 日志级别i info  d=debug  w=warning e=error
    logger.info('456')
    logger.debug('123')
    logger.warning('789')
    logger.error('741')
