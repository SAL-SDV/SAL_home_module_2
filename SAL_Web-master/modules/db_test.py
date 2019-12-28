#!/usr/bin/env python3
#coding:utf8
'''
L and D monitor. need.
for conn. parallel process.
'''
from time import sleep
from urllib.parse import urlparse
import mysql.connector
import datetime
import time
import serial

p=0
while(True):
    url = urlparse('mysql://pi:raspberry@localhost:3306/boso')
    conn = mysql.connector.connect(
        host = url.hostname,
        port = url.port,
        user = url.username,
        password = url.password,
        database = url.path[1:],
    )

    cur = conn.cursor()
    cur.execute('select * from sensor_config')
    sensor_list = cur.fetchall()
    sensor_list = [sensor_list[i][0] for i in range(len(sensor_list))]

    ser = serial.Serial('/dev/ttyUSB0',115200)
    test = str(ser.readline())
    print(test)
    slicer = test[13:21]
    cur = conn.cursor()

    checkflag = [flag for flag in range(len(sensor_list)) if str(sensor_list[flag]) == slicer]

    try:
        p=p+1
        print(slicer)
        print("start:try "+str(p))
        date = datetime.datetime.today()
        today = date.strftime('%Y-%m-%d')
        now = date.strftime('%H:%M:%S')
        cur.execute('insert into sensor (date,time,place) values (%s,%s,%s)',(str(today),str(now),str(slicer)))

        conn.commit()
    except IndexError:
        while True:
            print('This is new sensor. please give a name to this sensor.')
            place = input('>>>')
            if 0 < len(place) < 21: break
        cur.execute('insert into sensor_config (sensorID,door_name) values (%s,%s)',(str(slicer),str(place)))
        conn.commit()
        cur.execute('select * from sensor_config')
        sensor_list = cur.fetchall()
        sensor_list = [sensor_list[i][0] for i in range(len(sensor_list))]
    ser.close()
    sleep(4)
