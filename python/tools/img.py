#-*- coding:utf-8 -*-
# import image
import glob
import os
from PIL import Image
#按比例缩放 
def timage():
	for files in glob.glob('D:/test/*jpg'):
		# print(files)
		
		filepath,filename = os.path.split(files)
		filterame,ext = os.path.splitext(filename)
		print(filepath)
		print(filename)
		print(filterame)
		print(ext)
		
		opfile = r'D:/test/cut/'
		if(os.path.isdir(opfile)==False):
			os.mkdir(opfile)
		
		im = Image.open(files)
		
		w,h = im.size
		im_ss = im.resize((int(w*0.5),int(h*0.5)))
		im_ss.save(opfile + filterame + '.jpg')
		
		
timage()

os.system("pause")