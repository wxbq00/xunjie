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
		pdf_word = cls.driver.find_element_by_xpath('/html/body/section[2]/ul[1]/li[1]/a')
		pdf_word.click()



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
	def test_a_pdf_word(self):
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表
		self.driver.find_element_by_name('file').click()

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转word每一页')

	@Screen(driver)
	def test_b_pdf_word_jishu(self):

		radio=self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[3]')

		radio.click()
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转word奇数页')

	@Screen(driver)
	def test_c_pdf_word_oushu(self):

		radio=self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[4]')
		radio.click()
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转word偶数页')

	@Screen(driver)
	def test_d_pdf_word_zhiding(self):

		radio=self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[5]')
		radio.click()
		input=self.driver.find_element_by_id('inputagerange')
		input.send_keys('1,3')
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转word第1和第3页')

	@Screen(driver)
	def test_e_pdf_ppt(self):

		pdf_ppt=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[3]')
		pdf_ppt.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转ppt每一页')

	@Screen(driver)
	def test_f_pdf_ppt_jishu(self):
		radio = self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[3]')
		radio.click()
		pdf_ppt=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[3]')
		pdf_ppt.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转ppt奇数页')

	@Screen(driver)
	def test_g_pdf_ppt_oushu(self):

		radio=self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[4]')
		radio.click()
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转ppt偶数页')

	@Screen(driver)
	def test_h_pdf_ppt_zhiding(self):

		radio=self.driver.find_element_by_xpath('/html/body/main/section/div/div[2]/div[1]/a[5]')
		radio.click()
		input=self.driver.find_element_by_id('inputagerange')
		input.send_keys('1,3')
		list_name = []
		file=listdir(fileDir, list_name,['.pdf'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转ppt第1和第3页')

	@Screen(driver)
	def test_i_pdf_excel(self):

		pdf_excel=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[4]')
		pdf_excel.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转excel每一页')

	@Screen(driver)
	def test_j_pdf_html(self):

		pdf_html=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[5]')
		pdf_html.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转html每一页')

	@Screen(driver)
	def test_k_pdf_pic(self):

		pdf_pic=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[6]')
		pdf_pic.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()

		log.info('pdf转pic每一页')

	@Screen(driver)
	def test_l_pdf_txt(self):

		pdf_txt=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[7]')

		pdf_txt.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.pdf'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pdf转txt每一页')

	@Screen(driver)
	def test_m_word_pdf(self):

		word_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[8]')

		word_pdf.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.docx','.doc'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('word转pdf每一页')

	@Screen(driver)
	def test_n_excel_pdf(self):

		excel_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[9]')

		excel_pdf.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['xls','.xlsx'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('excel转pdf每一页')

	@Screen(driver)
	def test_o_ppt_pdf(self):

		ppt_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[10]')

		ppt_pdf.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.ppt','.pptx'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('ppt转pdf每一页')

	@Screen(driver)
	def test_p_pic_pdf(self):

		pic_pdf=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[1]/dd[11]')

		pic_pdf.click()
		list_name=[]
		file = listdir(fileDir, list_name, ['.jpg','.png','.bmp'])  # 文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pic转pdf每一页')







	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ == '__main__':
	unittest.main()










