# -*- coding: utf-8 -*-

import os
import time

project_list = ['test','y',"ss"] #����Ŀ���ƴ�����б���
print "������Ŀ���ƣ�"+ str(project_list)
#�����ļ����Ŀ¼
test = "D:\\AAA\\A\\"	#��ĿA
y = "D:\\AAA\\B\\"	#��ĿB

projectName = raw_input('��������Ҫ���ݵ���Ŀ���ƣ�') #������Ҫ���ݵ���Ŀ����
Source_File = "F:\\TEST\\Python\\" + projectName # ��Ҫ���ݵ���Ŀ����·��


if projectName == 'test':
	target = test + projectName + "_" + time.strftime('%Y%m%d%H%M%S') + '.rar'	#�����ļ�������ʽ����Ŀ��+ʱ��
	
	rar_command = "WinRAR a -r -ep1 %s %s" % (target,Source_File)	
	 
	# Run the backup
	if os.system(rar_command) == 0:		#ִ�б���
		print 'Successful backup to', target
		
		mysql_command = "mysqldump -uroot -p123456 test > " + test + projectName + ".sql"
		if os.system(mysql_command) == 0:		#ִ�б���
			print 'Successful backup to SQL'
		else:
			print "SQLfile backup fail"	
	else:
		print 'Project Backup FAILED'
	raw_input("��������˳�")
	
elif projectName == 'y':
	target = y + projectName + "_" + time.strftime('%Y%m%d%H%M%S') + '.rar'	#�����ļ�������ʽ����Ŀ��+ʱ��
	
	rar_command = "WinRAR a -r -ep1 %s %s" % (target,Source_File)	
	 
	# Run the backup
	if os.system(rar_command) == 0:		#ִ�б���
		print 'Successful backup to', target
		
		mysql_command = "mysqldump -uroot -p123456 test > " + y + projectName + ".sql"
		if os.system(mysql_command) == 0:		#ִ�б���
			print 'Successful backup to SQL'
		else:
			print "SQLfile backup fail"				
	else:
		print 'Project Backup FAILED'
	raw_input("��������˳�")
else:
	print "��Ŀ������"
	raw_input("��������˳�")	
