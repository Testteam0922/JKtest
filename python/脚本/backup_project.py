# -*- coding: utf-8 -*-

import os
import time

project_list = ['test','y',"ss"] #将项目名称存放在列表中
print "现有项目名称："+ str(project_list)
#备份文件存放目录
test = "D:\\AAA\\A\\"	#项目A
y = "D:\\AAA\\B\\"	#项目B

projectName = raw_input('请输入需要备份的项目名称：') #输入需要备份的项目名称
Source_File = "F:\\TEST\\Python\\" + projectName # 需要备份的项目所在路径


if projectName == 'test':
	target = test + projectName + "_" + time.strftime('%Y%m%d%H%M%S') + '.rar'	#备份文件命名方式：项目名+时间
	
	rar_command = "WinRAR a -r -ep1 %s %s" % (target,Source_File)	
	 
	# Run the backup
	if os.system(rar_command) == 0:		#执行备份
		print 'Successful backup to', target
		
		mysql_command = "mysqldump -uroot -p123456 test > " + test + projectName + ".sql"
		if os.system(mysql_command) == 0:		#执行备份
			print 'Successful backup to SQL'
		else:
			print "SQLfile backup fail"	
	else:
		print 'Project Backup FAILED'
	raw_input("按任意键退出")
	
elif projectName == 'y':
	target = y + projectName + "_" + time.strftime('%Y%m%d%H%M%S') + '.rar'	#备份文件命名方式：项目名+时间
	
	rar_command = "WinRAR a -r -ep1 %s %s" % (target,Source_File)	
	 
	# Run the backup
	if os.system(rar_command) == 0:		#执行备份
		print 'Successful backup to', target
		
		mysql_command = "mysqldump -uroot -p123456 test > " + y + projectName + ".sql"
		if os.system(mysql_command) == 0:		#执行备份
			print 'Successful backup to SQL'
		else:
			print "SQLfile backup fail"				
	else:
		print 'Project Backup FAILED'
	raw_input("按任意键退出")
else:
	print "项目不存在"
	raw_input("按任意键退出")	
