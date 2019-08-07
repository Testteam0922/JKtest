#coding:utf-8
import os
import qrcode
import PIL
import time
from os import listdir
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tools import file_read
from docx import Document
from docx.shared import Inches


data_file = ".\\data\\lock_num.xlsx"
listdata  = file_read.excel_read(filepath = data_file)
#print(listdata)


for i in range(len(listdata)):
	#生成二维码
	qr = qrcode.QRCode(     
	version=1,      #二维码大小
	error_correction=qrcode.constants.ERROR_CORRECT_L,     
	box_size=300,    #每个方格的像素大小  
	border=1,		#边框的厚度
	)

	locknum = listdata[i]['lock_num']
	imgpath = ".\\img\\" + locknum + ".png"
	font = ImageFont.truetype('.\\tools\\simsun.ttf',550)

	print(locknum)
	qr.add_data(locknum) 
	qr.make(fit=True)  
	img = qr.make_image()
	img = img.convert("RGBA")
	width,height =  img.size

	n_img= Image.new("RGBA", (width, height+500),"#FFFFFF")
	n_img.paste(img,(0,0))
	#n_img.show()

	#给图片编号
	draw = ImageDraw.Draw(n_img)
	draw.text((50,height-100),locknum,(0,0,0),font)
	#n_img.show()
	#保存图片
	n_img.save(imgpath)
print("二维码批量处理任务已完成")
print("---------------------------------------")
input("按任意键退出")

'''
挂锁配置：border=4，font：字体100，位置(100,870)
防盗锁配置：border=2，font：字体50，位置(220,815)
'''




'''
for i in range(len(listdata)):
	locknum = listdata[i]['lock_num']
	print (locknum)
	img = qrcode.make(locknum)
	img.save(".\\img\\" + locknum + '.png')

print("二维码已批量生成")
input("按任意键退出")


n_im= Image.new("RGB", (128, 128),"green")
n_im.show()
'''

