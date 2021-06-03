import cv2
import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqttClient
import time, RPi.GPIO as GPIO
import spidev
import numpy


def proccess_end(buzzer):
    pwm = GPIO.PWM(buzzer, 1.0)
    pwm.start(100.0)

    pwm.ChangeDutyCycle(90)

    pwm.ChangeFrequency(261)
    time.sleep(0.5)
    pwm.ChangeFrequency(329)
    time.sleep(0.5)
    pwm.ChangeFrequency(392)
    time.sleep(0.5)
    pwm.ChangeFrequency(523)
    time.sleep(0.5)

    pwm.stop()


def Alert_end(buzzer):
    pwm = GPIO.PWM(buzzer, 1.0)
    pwm.start(100.0)

    pwm.ChangeDutyCycle(90)

    pwm.ChangeFrequency(523)
    time.sleep(0.5)
    pwm.ChangeFrequency(392)
    time.sleep(0.5)
    pwm.ChangeFrequency(523)
    time.sleep(0.5)
    pwm.ChangeFrequency(392)
    time.sleep(0.5)

    pwm.stop()


def LCD_String(String):
    result = String.encode('utf-8')
    return result


pot_channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000


def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1
    r = spi.xfer2([1, 8+adcnum <<4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data


def send_frame():
    ip = "192.168.0.80"

    cap = cv2.VideoCapture(-1)

    if not cap.isOpened():
        print("Camera open failed..")
        sys.exit()

    if cap.isOpened():
        for _ in range(3):
            pot_value = readadc(pot_channel)
            success, frame = cap.read()
            if success:
                if pot_value > 200:
                    cv2.imshow("pi", frame)
                    img = bytearray(frame)
                    publish.single("data/streaming", img, hostname=ip)
                else:
                    val = 80
                    array = numpy.full(frame.shape, (val, val, val), dtype=numpy.uint8)
                    addFrame = cv2.add(frame, array)
                    cv2.imshow("pi", addFrame)
                    img = bytearray(addFrame)
                    publish.single("data/streaming", img, hostname=ip)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()


class ReceiveSign:
    def __init__(self):
        self.run_flag = True
        self.signVal = ""
        Broker = "192.168.0.80"
        client = mqttClient.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(Broker, 1883, 60)

        while self.run_flag:
            client.loop(0.01)


    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc));
        if rc == 0:
            client.subscribe("data/DB");
        else:
            print("Connect Fail");

    def on_message(self, client, userdata, msg):
        try:
            self.signVal = msg.payload.decode("utf-8")
            self.run_flag = False
        except Exception as e:
            print("Error..: ", e)

    def result_val(self):
        return self.signVal


class MaskSign:
    def __init__(self):
        self.run_flag = True
        self.signVal = ""
        Broker = "192.168.0.80"
        client = mqttClient.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(Broker, 1883, 60)

        while self.run_flag:
            client.loop(0.01)


    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc));
        if rc == 0:
            client.subscribe("data/mask");
        else:
            print("Connect Fail");

    def on_message(self, client, userdata, msg):
        try:
            self.signVal = msg.payload.decode("utf-8")
            self.run_flag = False
        except Exception as e:
            print("Error..: ", e)

    def result_val(self):
        return self.signVal