#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import time as tm
import paramiko
import scp as scp

#市役所サーバ（想定）の情報
hostname = '202.17.19.236'
port = 19122
username = 'sdv2019a'
password = 'HIbIbymQ2SAH'

#画像の転送
def send(path):
    #sshを用いて親機へファイルを転送
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(path,'/var/www/html/2019a/HomePhotoIn')
    print("scp_OK!")

if __name__ == '__main__':
    #path='/home/pi/SAL/viewer/public/images/2019:03:19:22:23:40.jpg'
    #send(path)
    print("NO!")
