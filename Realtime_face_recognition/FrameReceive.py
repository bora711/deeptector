import numpy as np
import paho.mqtt.client as mqttClient
from real_time_face_recognition import stream
from DBinput import update_info as update
import threading
from collections import deque


class ReceiveSensor:
    def __init__(self):
        self.BodyTemp = 0.0
        self.run_flag = True

        Broker = "172.30.1.16"
        client = mqttClient.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(Broker, 1883, 60)

        while self.run_flag:
            client.loop(0.01)

    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc));
        if rc == 0:
            client.subscribe("data/sensor");
        else:
            print("Connect Fail");

    def on_message(self, client, userdata, msg):
        try:
            self.BodyTemp = msg.payload.decode("utf-8")
            self.BodyTemp = float(self.BodyTemp)
            self.run_flag = False

        except Exception as e:
            print("Error..: ", e)

    def bodyTemp_return(self):
        result = self.BodyTemp
        return result




class ReceiveStreaming:
    def __init__(self):
        Broker = "172.30.1.16"
        self.frame = None
        self.run_flag = True

        client = mqttClient.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(Broker, 1883, 60)

        while self.run_flag:
            client.loop(0.01)

    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc));
        if rc == 0:
            client.subscribe("data/streaming");
        else:
            print("Connect Fail");

    def on_message(self, client, userdata, msg):
        try:
            self.frame = msg.payload
            self.run_flag = False

        except Exception as e:
            print("Error..: ", e)
            if msg.payload.decode("utf-8") == "exit":
                self.run_flag = False

    def frame_resource(self):
        return self.frame

def Ai_thread(frame, BodyTemp):

    frame = np.frombuffer(frame, dtype=np.uint8)
    frame = frame.reshape(480, 640, 3)

    camera_source = 0
    pb_path = r".\Face_Recognition3\pb_model.pb"
    node_dict = {'input': 'input:0',
                     'keep_prob': 'keep_prob:0',
                     'phase_train': 'phase_train:0',
                     'embeddings': 'embeddings:0',
                     }

    ref_dir = r".\database"
    stream(frame, BodyTemp, pb_path, node_dict, ref_dir, camera_source=camera_source, resolution="720", to_write=False,
           save_dir=None)



if __name__ == '__main__':
    while True:
        BodyTemp = ReceiveSensor().bodyTemp_return()
        print(BodyTemp)

        frameList = deque()
        for _ in range(5):
            receive = ReceiveStreaming().frame_resource()
            frameList.append([receive])

        while frameList:
            cur = frameList.popleft()
            Ai_thread(cur[0], BodyTemp)


