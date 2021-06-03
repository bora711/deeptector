import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import pygame
import spidev, serial, time

from smbus import SMBus
from mlx90614 import MLX90614

from RaspTool import send_frame
from RaspTool import ReceiveSign
from RaspTool import proccess_end
from RaspTool import LCD_String
from RaspTool import Alert_end

### GPIO Pin number 설정 ###
buzzer = 12
GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

### i2c 채널 설정 ###
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

### MCP3208 채널 중 센서에 연결한 채널 설정 ###
pot_channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000


### 시리얼 통신 ###
PORT = "/dev/ttyACM0"
BaudRate = 9600
ARD = serial.Serial(PORT, BaudRate)

ip = "192.168.0.80"

bodyTemp = 0.0
run_flag = True

bodyTemp = float("%0.2f" % sensor.get_object_1()) + 1.0

if bodyTemp > 37.5:
    pygame.mixer.init()
    pygame.mixer.music.load("ttsTest/test1.mp3")
    pygame.mixer.music.play()

while run_flag:
    bodyTemp = float("%0.2f" % sensor.get_object_1()) + 1.0
    if bodyTemp < 34.0 or bodyTemp > 37.5:
        pass
    else:
        run_flag = False

bus.close()

publish.single("data/sensor", bodyTemp, hostname=ip)

if bodyTemp != 0.0:
    proccess_end(buzzer)
    stage1 = LCD_String("Deeptect Start!")
    ARD.write(stage1)

    send_frame()

    result = ReceiveSign().result_val()
    print(result)

    stage2 = LCD_String("Deeptect Finish!")
    ARD.write(stage2)

    if result != "Mask":
        time.sleep(3)
        Alert_end(buzzer)
        stage1 = LCD_String("No Entry!")
        ARD.write(stage1)


    elif result == "Mask":
        time.sleep(3)
        proccess_end(buzzer)
        stage2 = LCD_String("Welcome!")
        ARD.write(stage2)

    stage2 = LCD_String("")
    ARD.write(stage2)
    GPIO.cleanup()

else:
    pass

stage2 = LCD_String("")
ARD.write(stage2)
GPIO.cleanup()

