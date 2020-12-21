#!/usr/bin/env python
# モジュール読み込み
import datetime
import time

import pymysql.cursors
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

while 1:
    zaishitu = 0

    # 現在時刻
    dt_now = datetime.datetime.now()

    # 在室の判断
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        if 'true' in text:
            reader.write("false")
            zaishitu = 0
        elif 'false' in text:
            reader.write("true")
            zaishitu = 1
    finally:
        GPIO.cleanup()

    print("read")

    # MySQLに接続する
    connection = pymysql.connect(
        host='localhost',
        user='COSMOS',
        password='PASSWORD',
        db='room_management',
        charset='utf8'
    )

    # Insert処理
    with connection.cursor() as cursor:
        sql = 'INSERT INTO zaishitu VALUES (%s, %s, %s)'
        cursor.execute(sql, (dt_now, id, zaishitu))
        # autocommitではないので、明示的にコミットする
        connection.commit()

    # MySQLから切断する
    connection.close()
    time.sleep(2)

# https://pimylifeup.com/raspberry-pi-rfid-rc522/

# https://qiita.com/utti0307/items/8abbea38bf78ff4abfa0
# https://qiita.com/johndoe1022/items/0c704a64a38d876e8bdf
# https://www.google.com/search?client=ms-android-samsung-ss&sxsrf=ALeKk01EGYCg3H2Q6gayqkUNqX8wdlz4wQ%3A1608573337105&ei=meHgX4ziBdbWhwP71beICA&q=python+mariadb&oq=python+Maria&gs_lcp=ChNtb2JpbGUtZ3dzLXdpei1zZXJwEAEYADICCAAyAggAMgIIADICCAAyAggAMgUIABDLATIFCAAQywEyBQgAEMsBOgQIABBHOgQIIxAnOgoIABCxAxCDARAEOgoIABCxAxCDARBDOgQIABAEOgQIABBDOggIABCxAxCDAToFCAAQsQNQvSNY2XFgyH5oAHABeACAAZQCiAGNDJIBBTAuMS42mAEAoAEByAEEwAEB&sclient=mobile-gws-wiz-serp
