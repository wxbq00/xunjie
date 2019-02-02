from selenium import webdriver
from time import sleep
from login import Login
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from config.browser import  DRIVER_PATH

from log.log import Log
from two_time_package import Yoyo
import os
fileDir=r'C:\Users\Administrator\PycharmProjects\xunjie\file'
abspath = os.path.abspath(fileDir)
allfile = os.listdir(fileDir)# 文件名
import random
from config.screen import Screen
log=Log()
from BeautifulReport import BeautifulReport

def listdir(path, list_name, filetype):#路径和文件名拼接
	for file in os.listdir(path):#列出文件目录
		file_path = os.path.join(path, file)#路径和文件名拼接

		if os.path.isdir(file_path):  # 判断路径是否是目录
			listdir(file_path, list_name,filetype)
		elif os.path.splitext(file_path)[1] in filetype:#分割路径，返回文件扩展名的元组
			list_name.append(file_path)
	if len(list_name)>4:
		list_name = random.sample(list_name, 4)#取随机4个文件名
	return list_name#文件名


class pdf_convert(unittest.TestCase):

	driver = webdriver.Chrome(DRIVER_PATH)

	logger=Log()
	@classmethod
	def setUpClass(cls):

		Login().user_login(cls.driver)
		pdf_hebin=cls.driver.find_element_by_xpath('/html/body/section[2]/ul[5]/li[1]/a')
		pdf_hebin.click()


	def public(self):
		time.sleep(3)
		convert_button = self.driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a')
		convert_button.click()
		time.sleep(30)
		dwnbtn = self.driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]')

		dwnbtn_is_appeared = WebDriverWait(self.driver,60).until(
			lambda x: x.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]').is_displayed())  # 下载按钮

		self.assertTrue(dwnbtn_is_appeared)
		dwnbtn.click()

	@Screen(driver)
	def test_a_pdf_hebin(self):
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf合并')

	@Screen(driver)
	def test_b_pdf_fenge(self):
		pdf_fenge=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[3]/a/span')
		pdf_fenge.click()
		list_name = []
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf分割')

	@Screen(driver)
	def test_c_pdf_psw_add(self):
		pdf_psw_add = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[5]/a/span')
		pdf_psw_add.click()
		input_text=self.driver.find_element_by_id('inputpdfpwd')
		input_text.send_keys('123')
		list_name = []
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf增加密码')



	@Screen(driver)
	def test_d_pdf_getpic(self):
		pdf_getpic = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[7]/a/span')
		pdf_getpic.click()

		list_name = []
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf图片获取')





	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ == '__main__':
	unittest.main()