# モジュール読み込み
import datetime

import pymysql.cursors

# 現在時刻
dt_now = datetime.datetime.now()

print(dt_now)

# MySQLに接続する
connection = pymysql.connect(
    host='192.168.11.7',
    user='COSMOS',
    password='PASSWORD',
    db='room_management',
    charset='utf8'
)

# Insert処理
with connection.cursor() as cursor:
    sql = "INSERT INTO zaishitu VALUES (%s, %s, %s)"
    cursor.execute(sql, (dt_now,  901, 0))
    # autocommitではないので、明示的にコミットする
    connection.commit()

# MySQLから切断する
connection.close()

