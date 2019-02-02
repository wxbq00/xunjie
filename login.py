import time
from selenium import webdriver
import configparser
import csv,xlrd

from selenium.webdriver.support.wait import WebDriverWait


class Login():

    def user_login(self,driver):

        url = 'http://app.xunjiepdf.com/'
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        login = driver.find_element_by_xpath('/html/body/section[1]/div/div/a[2]')
        login.click()
        username = driver.find_element_by_id('tb_memAccount')
        username.clear()
        username.send_keys('13098498721')
        userpasswd = driver.find_element_by_id('tb_memPwd')
        userpasswd.clear()
        userpasswd.send_keys('584521')
        loginbtn=driver.find_element_by_id('btn_formLoginAccount')
        loginbtn.click()
        time.sleep(2)
        firstPage=driver.find_element_by_xpath('//*[@id="hader-nav"]/li[2]/a')
        firstPage.click()


login=Login()


