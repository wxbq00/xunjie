from selenium import webdriver
from time import sleep
from login import Login
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from config.browser import  DRIVER_PATH

from log.log import Log
from two_time_package import Yoyo
from config.screen import Screen
import os
fileDir=r'C:\Users\Administrator\PycharmProjects\xunjie\file'
abspath = os.path.abspath(fileDir)
allfile = os.listdir(fileDir)# 文件名
import random
log=Log()

def listdir(path, list_name, filetype):
	for file in os.listdir(path):
		file_path = os.path.join(path, file)

		if os.path.isdir(file_path):  # 子目录
			listdir(file_path, list_name,filetype)
		elif os.path.splitext(file_path)[1] in filetype:
			list_name.append(file_path)
	if len(list_name)>4:
		list_name = random.sample(list_name, 4)
	return list_name


class wps_caj_cad(unittest.TestCase):
	driver = webdriver.Chrome(DRIVER_PATH)
	logger=Log()
	@classmethod
	def setUpClass(cls):

		Login().user_login(cls.driver)
		pdf_word = cls.driver.find_element_by_xpath('/html/body/section[2]/ul[1]/li[1]/a')
		pdf_word.click()


	def public(self):
		time.sleep(3)
		convert_button = self.driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a')
		convert_button.click()

		dwnbtn = self.driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]')

		dwnbtn_is_appeared = WebDriverWait(self.driver,80).until(
			lambda x: x.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]').is_displayed())  # 下载按钮


		self.assertTrue(dwnbtn_is_appeared)
		dwnbtn.click()

	# @Screen(driver)
	# def test_a_wps_office(self):
	# 	wps_office=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[2]/dd[2]')
	# 	wps_office.click()
	# 	list_name = []
	# 	type=['.doc','.docx','.wps','.et','.dps']
	# 	b = random.sample(type, 4)
	#
	# 	file=listdir(fileDir, list_name,b)#文件名的列表
	#
	#
	# 	for i in file:
	# 		self.driver.find_element_by_name('file').send_keys(i)
	# 	self.public()
	# 	log.info('wps转office每一页')
	#
	# @Screen(driver)
	# def test_b_wps_pdf(self):
	# 	wps_office=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[2]/dd[3]')
	# 	wps_office.click()
	# 	list_name = []
	# 	type=['.doc','.docx','.wps','.et','.dps']
	# 	b = random.sample(type, 4)
	#
	# 	file=listdir(fileDir, list_name,b)#文件名的列表
	#
	#
	# 	for i in file:
	# 		self.driver.find_element_by_name('file').send_keys(i)
	# 	self.public()
	#
	# 	log.info('wps转pdf每一页')

	@Screen(driver)
	def test_c_caj_word(self):
		caj_word=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[3]/dd[2]')

		caj_word.click()
		list_name = []

		file=listdir(fileDir, list_name,['.caj'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('caj转word每一页')

	@Screen(driver)
	def test_d_caj_pdf(self):
		caj_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[3]/dd[3]')

		caj_pdf.click()
		list_name = []


		file=listdir(fileDir, list_name,['.caj'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('caj转pdf每一页')

	@Screen(driver)
	def test_e_cad_pdf(self):
		cad_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[4]/dd[2]')

		cad_pdf.click()
		list_name = []
		file=listdir(fileDir, list_name,['.dwg','.dwt','.dxf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('cad转pdf每一页')

	@Screen(driver)
	def test_f_cad_jpg(self):
		cad_jpg=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[4]/dd[3]')
		cad_jpg.click()
		list_name = []
		file=listdir(fileDir, list_name,['.dwg','.dwt','.dxf'])#文件名的列表
		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('cad转jpg每一页')

	@Screen(driver)
	def test_g_pdf_cad(self):
		pdf_cad=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[4]/dd[4]')

		pdf_cad.click()
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表
		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('pdf转cad每一页')

	@Screen(driver)
	def test_h_cad_cad(self):
		cad_cad = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[4]/dd[5]')

		cad_cad.click()
		list_name = []
		file = listdir(fileDir, list_name, ['.dwg','.dxf'])  # 文件名的列表
		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('cad转cad每一页')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ == '__main__':
	unittest.main()