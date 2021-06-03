import os
from pathlib import Path

import cv2
import base64
import time

from django.http import JsonResponse

from DBinput import memberDb

# src = cv2.imread('ImgData/image1.jpg', cv2.COLOR_BGR2RGB)
# print(type(src))
# src = cv2.resize(src, dsize=(320, 240), interpolation=cv2.INTER_AREA)
# cv2.imwrite('ImgData/image2.jpg', src)

def update_info(name, bodyTemp, state):
    id = "id01"

    with open("ImgData/image.jpg", "r+b") as f:
        chunk = f.read()

    sensorImg = base64.b64encode(chunk)

    sensorImg = sensorImg.decode('utf-8')
    print(sensorImg)

    enter_time = time.strftime("%c", time.localtime(time.time()))
    enter_time = enter_time[10:19]

    memberDb().update(sensorImg, name, enter_time, str(bodyTemp), str(state), id)

update_info("jaeeon", 34.37, "mask")