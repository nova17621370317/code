# _*_ coding: utf-8 _*_

from selenium import webdriver
import time

def loginBigdata(url):
    driver = webdriver.Chrome()
    driver.get(url)  # open the url
    print u'正在进入' + driver.title + '......'
    user_xpath = '//*[@id="userName"]'
    passwd_xpath = '//*[@id="login"]/form/div/div[2]/div/label/input'
    submit_xpath = '//*[@id="submit"]'
    ele = driver.find_element_by_xpath(user_xpath)  # location user box
    ele.clear()
    username = 'wbtest'
    password = 'pingjia123'
    ele.send_keys(username)
    ele = ele.find_element_by_xpath(passwd_xpath)   # location passwd box
    ele.clear()
    ele.send_keys(password)
    ele = ele.find_element_by_xpath(submit_xpath)
    ele.click()
    return driver

def overview(driver):
#    nav_overview = '//*[@id="nav-list"]/ul/li[1]/span'
    driver.find_element_by_class_name('menu-title').click()
#    thirty_days = '//*[@id="app"]/div[2]/div[2]/div/div[1]/label[1]/div/div[2]/div/label[2]/span'
    ele = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/label[1]/div/div[2]/div/label[2]/span').click()
    time.sleep(3)
    # activity_device = '/html/body/div[2]/div/div[1]/ul/li[2]/span'
    # driver.find_element_by_xpath(activity_device).click()
    # time.sleep(3)

# 对于异步的ajax出来的数据只能通过 源代码的方式获取 信息，因为下一次就不一样了

if __name__ == '__main__':
    url = 'http://bdp.chinaubi.com/auth/index.html#/statisticalAnalysis/wordcloud'
    driver = loginBigdata(url)
    overview(driver)
    driver.close()

