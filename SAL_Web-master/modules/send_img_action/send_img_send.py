#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import time as tm
import paramiko
import scp as scp

#ここでは自前のラズパイでテスト
hostname = '192.168.13.30'
port = 57532
username = 'pisa'
password = 'test_pass_8/7'

#画像の転送
def send(path):
    #sshを用いて親機へファイルを転送
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(path,'/home/pisa/img')
    print("rest")

if __name__ == '__main__':
    #このプログラムが直接呼び出された場合、適当なimgを転送する
    path='/home/pi/SAL/viewer/public/images/2019:03:19:22:23:40.jpg'
    send(path)
