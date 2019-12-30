#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import os
import datetime

#pathは'/home/pi/SAL_Web-master/media/images/000000_0000:00:00:00:00:00.jpg'のような形で入っている。
def registor(path):
    #接続先を指定
    con = mysql.connector.connect(
            host='localhost',
            user='user',
            passwd='user',
            db='sal')

    cur = con.cursor()

    dtstr = (path[-23:-4])
    dt = datetime.datetime.strptime(dtstr, '%Y:%m:%d:%H:%M:%S')

    cameraID = 1

    send_path = (''+path[-30:])

    info = [dt,send_path,cameraID]

    try:
            table = 'imagelist'
            '''
            cur.execute("DROP TABLE IF EXISTS %s;" % table)
            cur.execute(
            """
            CREATE TABLE %s(
            id int(10) auto_increment not null primary key,
            imagedata datetime,
            path varchar(255),
            cameraID varchar(20)
            )
            """ % table)
            '''
            cur.execute("INSERT INTO imagelist(imagedata,path,cameraID) VALUES('{0[0]}','{0[1]}','{0[2]}');".format(info))

            cur.execute("select * from imagelist")
            rows = cur.fetchall()
            for row in rows:
             print(row)

            con.commit()

    except mysql.connector.Error as err:
            print("Failed crete: {}".format(err))

    finally:
            con.close()

if __name__ == '__main__':
    #このプログラムが直接呼び出された場合、errorメッセージを表示する
    registor('/home/pi/SAL_Web-master/media/images/111001_2019:12:26:18:25:46.jpg')
    #pritnt("error:send_img_registor.py-this file only used by import ")
