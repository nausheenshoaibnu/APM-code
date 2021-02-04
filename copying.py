import os
import time
sudoPassword = 'syslab123'
while(len(os.listdir('openimage_yolo/result_img/'))>=0):
    if(len(os.listdir('openimage_yolo/result_img/')) >= 10):
        command = 'sudo docker cp openimage_yolo/result_img/ 250fc7581dab:/root/openface/'
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
	os.system('rm -r openimage_yolo/result_img/*')

