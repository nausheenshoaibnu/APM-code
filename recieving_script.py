import os
import time
sudoPassword = 'syslab123'
while(True):
    while(len(os.listdir('result_img/')) >= 300):
    	command = 'sudo docker cp result_img/ ff3c868006e8:/root/openface/'
    	p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
	os.system('rm -r result_img')
	os.makedirs('result_img')
