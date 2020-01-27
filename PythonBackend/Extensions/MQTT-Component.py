import time
import json
import paho.mqtt.client as mqtt


class MQTTClient():
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

    def connect(self):
        q = self.client.connect("169.254.248.10", 1883)
        return "Connection to localhost, Quality {i}".format(i=q)

    def init(self):
        pass

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

    def main(self):
        try:
            print(self.connect())
            time.sleep(4)
            print(self.subscriber("/RASPI/INTERN/CPU/TEMP"))
            self.client.loop_forever()

        finally:
            self.client.disconnect()



if __name__ == '__main__':

    c = MQTTClient()
    c.main()
