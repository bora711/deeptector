import MySQLdb
import time
import base64

import cv2

config = {
    'database': 'bigdata',
    'user': 'root',
    'password': 'elqxprxj@',
    'host': '13.209.179.184',
    'port': 624,
    'charset': 'utf8',
    'use_unicode': True
}

class Sql:
    updateInfo = """UPDATE member SET mask = '%s', name = '%s', in_enter = '%s', bodyTemp = '%s', state = '%s' WHERE id = '%s' """

class DB:
    def getConnection(self):
        conn = MySQLdb.connect(**config)
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            cursor.close();


class memberDb(DB):
    def update(self, id, mask, name, in_enter, bodyTemp, state):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.updateInfo % (id, mask, name, in_enter, bodyTemp, state))
            conn.commit()
        except:
            conn.rollback();
            raise Exception
        finally:
            super().close(conn, cursor)

def take_a_picture(img):
    filename = "ImgData/image.jpg"
    cv2.imwrite(filename, img)


def update_info(name, bodyTemp, state):
    id = "id01"

    with open("ImgData/image.jpg", "r+b") as f:
        chunk = f.read()

    sensorImg = base64.b64encode(chunk)

    sensorImg = sensorImg.decode('utf-8')

    enter_time = time.strftime("%c", time.localtime(time.time()))
    enter_time = enter_time[10:19]

    memberDb().update(sensorImg, name, enter_time, str(bodyTemp), str(state), id)