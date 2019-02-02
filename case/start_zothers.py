from selenium import webdriver
from time import sleep
from login import Login
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from config.browser import  DRIVER_PATH
from selenium.webdriver.support.select import Select
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


class other_convert(unittest.TestCase):
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
		time.sleep(40)
		dwnbtn = self.driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]')

		dwnbtn_is_appeared = WebDriverWait(self.driver,60).until(
			lambda x: x.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/a[3]').is_displayed())  # 下载按钮

		self.assertTrue(dwnbtn_is_appeared)
		dwnbtn.click()

	def js_scroll_top(self):
		'''滚动到顶部'''
		js = "var q=document.body.scrollTop=0"
		self.driver.execute_script(js)

	def js_scroll_end(self):
		'''滚动到底部'''
		js = "var q=document.body.scrollTop=10000"
		self.driver.execute_script(js)

	@Screen(driver)
	def test_a_heic_jpg(self):
		heic_jpg=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[2]')

		heic_jpg.click()
		list_name = []


		file=listdir(fileDir, list_name,['.heic'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('heic转jpg每一页')

	@Screen(driver)
	def test_b_word_longpic(self):
		word_longpic=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[3]')

		word_longpic.click()
		list_name = []


		file=listdir(fileDir, list_name,['.doc','.docx'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('word转长图')

	@Screen(driver)
	def test_c_ppt_longpic(self):
		ppt_longpic=self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[4]')
		ppt_longpic.click()
		list_name = []


		file=listdir(fileDir, list_name,['.ppt','.pptx'])#文件名的列表


		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('ppt转长图')

	@Screen(driver)
	def test_d_pic_jpg(self):
		pic_jpg = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[5]')

		pic_jpg.click()
		list_name = []

		file = listdir(fileDir, list_name, ['.png', '.bmp','.ico'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pic转jpg')

	@Screen(driver)
	def test_e_pic_png(self):
		pic_png = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[6]')

		pic_png.click()
		list_name = []

		file = listdir(fileDir, list_name, ['.jpg', '.bmp','.ico'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pic转png')

	@Screen(driver)
	def test_f_pic_bmp(self):
		pic_bmp = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[7]')

		pic_bmp.click()
		list_name = []

		file = listdir(fileDir, list_name, ['.png', '.jpg','.ico'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pic转bmp')

	@Screen(driver)
	def test_g_pic_icon(self):
		pic_icon = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[5]/dd[8]')

		pic_icon.click()
		list_name = []

		file = listdir(fileDir, list_name, ['.png', '.bmp','.jpg'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('pic转icon')

	# @Screen(driver)
	# def test_h_ppt_video(self):
	# 	ppt_video = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[2]')
	#
	#
	# 	ppt_video.click()
	# 	list_name = []
	#
	# 	file = listdir(fileDir, list_name, ['.ppt', '.pptx'])  # 文件名的列表
	#
	# 	for i in file:
	# 		self.driver.find_element_by_name('file').send_keys(i)
	# 	self.public()
	# 	log.info('ppt转video')
	#
	# @Screen(driver)
	# def test_i_video_gif(self):
	# 	video_gif = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[3]')
	#
	#
	# 	video_gif.click()
	# 	list_name = []
	#
	# 	file = listdir(fileDir, list_name, ['.ogg', '.mp4','.m4v','.webm'])  # 文件名的列表
	#
	#
	# 	self.driver.find_element_by_name('file').send_keys(r'C:\Users\Administrator\PycharmProjects\xunjie\file\video\xxx.mp4')
	# 	time.sleep(2)
	# 	qutu=self.driver.find_element_by_xpath('/html/body/main/section/div/section[1]/div[1]/div[2]/span[1]')
	# 	qutu.click()
	# 	cancel=self.driver.find_element_by_xpath('/html/body/main/section/div/section[1]/div[1]/div[2]/span[2]')
	# 	time.sleep(3)
	# 	cancel.click()
	# 	convertBtn=self.driver.find_element_by_xpath('/html/body/main/section/div/section[1]/div[1]/div[2]/span[3]')
	# 	convertBtn.click()
	# 	dwnbtn=self.driver.find_element_by_xpath('/html/body/main/section/div/section[1]/div[1]/div[2]/a[2]')
	# 	dwnbtn_is_appeared = WebDriverWait(self.driver, 50).until(
	# 		lambda x: x.find_element_by_xpath('/html/body/main/section/div/section[1]/div[1]/div[2]/a[2]').is_displayed())  # 下载按钮
	#
	# 	self.assertTrue(dwnbtn_is_appeared)
	# 	dwnbtn.click()
	#
	# 	log.info('video转gif')
	#
	# @Screen(driver)
	# def test_j_video_video(self):
	# 	video_video = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[4]')
	#
	# 	video_video.click()
	# 	list_name = []
	# 	type = ['.mov', '.mp4','.mkv','.avi','.wmv','.m4v']
	# 	b = random.sample(type, 4)
	# 	file = listdir(fileDir, list_name, b)  # 文件名的列表
	# 	selectbox=self.driver.find_element_by_id('videoformatchose')
	# 	Select(selectbox).select_by_value('mpeg')
	# 	for i in file:
	# 		self.driver.find_element_by_name('file').send_keys(i)
	#
	# 	self.public()
	# 	log.info('video转video')
	#
	# @Screen(driver)
	# def test_k_audio_audio(self):
	# 	audio_audio = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[5]')
	#
	# 	audio_audio.click()
	# 	list_name = []
	# 	type = ['.mav', '.mp3','.ogg','.m4a','.wma']
	# 	b = random.sample(type, 4)
	# 	file = listdir(fileDir, list_name, b)  # 文件名的路径列表
	# 	selectbox = self.driver.find_element_by_id('videoformatchose')
	# 	Select(selectbox).select_by_value('m4a')
	# 	for i in file:
	# 		self.driver.find_element_by_name('file').send_keys(i)
	#
	#
	# 	self.public()
	# 	log.info('audio转audio')

	@Screen(driver)
	def test_h_book_pdf(self):
		book_pdf = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[2]')


		book_pdf.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.mobi','.azw3'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转pdf')

	@Screen(driver)
	def test_i_book_txt(self):
		book_txt = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[3]')


		book_txt.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.mobi','.azw3'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转txt')

	@Screen(driver)
	def test_j_book_word(self):
		book_word = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[4]')

		book_word.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.mobi','.azw3'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转word')

	@Screen(driver)
	def test_k_book_mobi(self):
		book_mobi = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[5]')

		book_mobi.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.docx','.azw3','.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转mobi')

	@Screen(driver)
	def test_l_book_epub(self):
		book_epub = self.driver.find_element_by_xpath('/html/body/main/section/aside/div/dl[6]/dd[6]')

		book_epub.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['mobi','.docx','.azw3','.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转epub')

	@Screen(driver)
	def test_m_book_azw3(self):
		book_azw3 = self.driver.find_element_by_xpath('	/ html / body / main / section / div[1] / div / dl[6] / dd[7]')


		book_azw3.click()
		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.docx','.mobi','.pdf'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('book转azw3')
		time.sleep(3)

	@Screen(driver)
	def test_n_epub_txt(self):


		epub_txt = self.driver.find_element_by_xpath('/html/body/main/section/div[1]/div/dl[6]/dd[8]')


		epub_txt.click()

		list_name=[]

		file = listdir(fileDir, list_name, ['.epub','.azw3','.mobi'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('epub转txt')
		time.sleep(3)

	@Screen(driver)
	def test_o_txt_epub(self):

		txt_epub = self.driver.find_element_by_xpath('/ html / body / main / section / aside / div / dl[6] / dd[9]')




		txt_epub.click()

		list_name=[]

		file = listdir(fileDir, list_name, ['.txt'])  # 文件名的列表

		for i in file:
			self.driver.find_element_by_name('file').send_keys(i)
		self.public()
		log.info('txt转epub')


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
