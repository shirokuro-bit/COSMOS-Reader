#!/usr/bin/env python
# モジュール読み込み
import datetime
import time

import pymysql.cursors
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

config = {
    'user': 'COSMOS',
    'password': 'PASSWORD',
    'host': 'localhost',
    'database': 'room_management',
    'charset': 'utf8'
}

while 1:
    zaishitu = 0

    # 現在時刻
    dt_now = datetime.datetime.now()

    # RFID取得
    reader = SimpleMFRC522()
    try:
        rfid, text = reader.read()
        if 'true' in text:
            reader.write("false")
            zaishitu = 0
        elif 'false' in text:
            reader.write("true")
            zaishitu = 1
    finally:
        GPIO.cleanup()
        print("読み込み完了")

    # 在室情報のInsert処理
    def query(sql, args):
        with connection.cursor() as cursor:
            cursor.execute(sql, args)
            connection.commit()

    # MySQLに接続する
    connection = pymysql.connect(**config)

    # RFIDの有無の確認
    with connection.cursor() as cursor:
        # query('select * from username where rfid_id = %s', rfid)
        sql_1 = 'select * from username where rfid_id = %s'
        cursor.execute(sql_1, rfid)
        # autocommitではないので、明示的にコミットする
        connection.commit()

    print("あるか無いか")
    if str(cursor.fetchone()) == 'None':
        print("なかった")
        # RFIDの新規登録
        with connection.cursor() as cursor:
            query('INSERT INTO username VALUES (%s, %s)', (rfid, 'NULL'))

            zaishitu = 1
            reader.write("true")
            print("新規登録完了")

        query('INSERT INTO zaishitu VALUES (%s, %s, %s)', (dt_now, rfid, zaishitu))

    else:
        print("あった")
        query('INSERT INTO zaishitu VALUES (%s, %s, %s)', (dt_now, rfid, zaishitu))

    # MySQLから切断する
    connection.close()
    time.sleep(2)
