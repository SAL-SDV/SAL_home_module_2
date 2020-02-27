#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import hashlib
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
#更新にあわせて実行するモジュール
from send_img_action import send_img as send
from send_img_action import registor_img as registor
from send_img_action import movie_to_img as to_img

#複数回検知されないようようにハッシュを記録
hashes = {}

# 監視対象のファイル
observed_file_type = ('.h264')

# 設定
#BASEDIR = os.path.abspath(os.path.dirname(__file__))

#監視対象フォルダを指定
BASEDIR ='/home/pi/SAL_Web-master/media/movie'

# 変更したファイルが監視対象であるかを調べる
# ハッシュと比較して、同一ファイルでなければ実行する
def match(path):
    if(any([path.endswith(ft) for ft in observed_file_type])):
        with open(path,'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()
        if path not in hashes or (hashes[path] != checksum):
            hashes[path] = checksum
            return True
        else:
            return False
    else:
        return False

# 変更時のイベントハンドラ
class ChangeHandler(FileSystemEventHandler):
    #ファイル変更時に実行
    def on_modified(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        if match(filepath):
            print('Modified',filepath)
            img_path = to_img.change_img(filepath)  #有効画像抽出
            if(img_path):
                registor.registor(img_path) #DB登録
                #send.send(img_path) #ファイル転送

    """
    #ファイル削除時に実行
    def on_deleted(self, event):
        if event.is_directory:
            return
        if match(event.src_path):
            print('delete',event.src_path)
            time.sleep(10)
    """
if __name__ in '__main__':
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, BASEDIR, recursive=True)
    print('start dir=',BASEDIR)
    observer.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
