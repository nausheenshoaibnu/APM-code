import os, os.path
import tarfile
import shutil
from threading import Thread
import time


sudoPassword = 'syslab123'
i = 1
while(True):
    if(len(os.listdir('openimage_yolo/result_img/'))>= 300):
	flag = 0	
	if i == 1:   	
       	    command = 'sudo docker cp openimage_yolo/result_img 581e7f38d4e9:/root/openface/'
	if i == 2:
	    command = 'scp -r openimage_yolo/result_img/ syslab@10.0.0.2:~/Desktop/'
	if i == 3:
	    command = 'scp -r openimage_yolo/result_img/ syslab@10.0.0.1:~/Desktop/'
	    flag = 1
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
	os.system('cp -r openimage_yolo/result_img/ record5_multi/')
	os.system('rm -r openimage_yolo/result_img/*')
	i = i+1
	if flag == 1:
	    i = 1
