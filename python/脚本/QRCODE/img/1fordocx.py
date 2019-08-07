#coding:utf-8
import time
from os import listdir
from docx import Document
from docx.shared import Inches
from PIL import Image

document = Document()											#doc对象	
pictures = [fn for fn in listdir() if fn.endswith('.png')]
pictures.sort()
print (pictures)

for fn in pictures:
	document.add_picture(fn,width=Inches(1.5))#向文档里添加图片
document.save('..\\doc\\' + '二维码' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.docx')	#保存文档


input("`````````````````````")



