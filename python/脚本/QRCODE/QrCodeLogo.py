# encoding: utf-8

import time
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from tools import file_read


def gen_qrcode():
	'''
	生成中间带logo的二维码
	需要安装qrcode, PIL库
	param logo: logo文件路径

	'''
	data_file = ".\\data\\lock_num.xlsx"		#锁编号xlsx文档地址
	logo = ".\\logo\\logo.png"					#logo地址
	listdata  = file_read.excel_read(filepath = data_file)	#读取所有数据至列表
	
	for i in range(len(listdata)):   
		qr = qrcode.QRCode(						#设置二维码大小 version:图片大小，box_size：每个方格的像素大小，border:边框宽度
			version=2,
			error_correction=qrcode.constants.ERROR_CORRECT_H,
			box_size=30,
			border=4
		)
		font = ImageFont.truetype('.\\tools\\simsun.ttf',100)	#字体大小与类型（宋体文件）
		locknum = listdata[i]['lock_num']						#获取锁编号
		print(locknum)
		qr.add_data(locknum)
		qr.make(fit=True)

		img = qr.make_image()
		img = img.convert("RGBA")
		#给图片编号
		draw = ImageDraw.Draw(img)
		draw.text((120,860),locknum,(0,0,0),font)			#在二维码图片上添加字体，（200,830）：图片上字体的位置（单位像素，根据图片大小调整）

		if logo and os.path.exists(logo):					#二维码图片上添加logo
			icon = Image.open(logo)
			img_w, img_h = img.size
			factor = 4
			size_w = int(img_w / factor)
			size_h = int(img_h / factor)

			icon_w, icon_h = icon.size
			if icon_w > size_w:
				icon_w = size_w
			if icon_h > size_h:
				icon_h = size_h
			icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

			w = int((img_w - icon_w) / 2)
			h = int((img_h - icon_h) / 2)
			icon = icon.convert("RGBA")
			img.paste(icon, (w, h), icon)
		img.save(".\\img\\" + locknum + '.png')			#保存二维码
	print("任务已完成")
	input("按任意键退出")

if __name__ == "__main__":
   gen_qrcode()
