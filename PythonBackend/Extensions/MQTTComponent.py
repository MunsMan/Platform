import time
import json
import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, device_name):
        self.client = mqtt.Client()
        self.device_name = device_name
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.full_tree_scan_store = []
        self.topic_list = []

    def connect(self):
        q = self.client.connect("localhost", 1883)
        return "Connection to localhost, Quality {i}".format(i=q)

    def init(self):
        self.client.loop_start()

    def subscriber(self, topic):
        q = self.client.subscribe(topic)
        return "Subscribed to Topic {t} with the Quality {q}".format(t=topic, q=q)

    def on_message(self, client, userdata, msg):
        print(json.loads(msg.payload))

    def on_connect(self, client, userdata):
        """
        Logging for debugging
        :return:
        """
        pass

    def full_tree_scan(self):
        base_topic = "/{d}/#"
        self.client.subscribe(base_topic)
        pre_on_message = self.client.on_message
        self.client.on_message = self.on_message_scan
        print("listening for 10 sec for messages")
        time.sleep(10)
        data = self.full_tree_scan_store
        self.full_tree_scan_store = []
        self.client.on_message = pre_on_message
        return data

    def on_message_scan(self, client, userdata, msg):
        if msg.topic not in self.topic_list:
            self.topic_list.append(msg.topic)
            self.full_tree_scan_store.append({"topic": msg.topic, "timestamp": msg.timestamp, "data": msg.payload})

    def main(self):
        try:
            print("Connecting")
            print(self.connect())
            time.sleep(1)
            self.init()
            time.sleep(4)
            print(self.subscriber("/RASPI/INTERN/CPU/TEMP"))
            print(self.full_tree_scan())
            time.sleep(1)
            while True:
                time.sleep(1)

        finally:
            self.client.loop_stop()
            self.client.disconnect()


if __name__ == '__main__':
    c = MQTTClient("RASPI")
    c.main()
