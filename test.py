import os
dir=r'C:\Users\Administrator\PycharmProjects\xunjie\file'
import random

def detect_walk(dir_path):
    for parent,dirnames,files in os.walk(dir_path):
        print(files)

def listdir(path, list_name, filetype):
	for parent,dirnames,files in os.walk(path):
		for filename in files:
			file_path = os.path.join(path,filename)
			print(file_path)

			if os.path.isdir(file_path):  # 子目录
				listdir(file_path, list_name,filetype)
			elif os.path.splitext(file_path)[1] in filetype:
				list_name.append(file_path)

	if len(list_name)>4:
		list_name = random.sample(list_name, 4)
	#print(list_name)
	return list_name


if __name__ == "__main__":
	list_name=[]
	print(listdir(dir, list_name,['.pdf']))
	print(detect_walk(dir))


