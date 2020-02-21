#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

def registor(path):
    #接続先を指定
    con = mysql.connector.connect(
        host='192.168.13.30',
        user='pi',
        passwd='raspberry',
        db='Gdb')

    cur = con.cursor()

    #pathは'/home/pi/SAL/viewer/public/images/0000_00_00_00_00_00.jpg'のような形で入っているのでスライスで切り出す。
    date = ("201"+path[-20:-13])
    time = ""
    #timeの文字列を日付型に変換
    for a in path[-12:-4]:
        if a=="_":
            time += ":"
        else:
            time += a

    send_path = ("/home/pisa/img/"+"201"path[-20:])
    info = [date,time,send_path]

    try:
        table = '1_img'
        '''
        cur.execute("DROP TABLE IF EXISTS %s;" % table)
        cur.execute(
        """
        CREATE TABLE %s(
        id int(10) auto_increment not null primary key,
        date date,
        time time ,
        path varchar(50)
        )
        """ % table)
        '''
        cur.execute("INSERT INTO 1_img(date,time,path) VALUES('{0[0]}','{0[1]}','{0[2]}');".format(info))

        cur.execute("select * from 1_img")
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
    pritnt("error:send_img_registor.py-this file only used by import ")
