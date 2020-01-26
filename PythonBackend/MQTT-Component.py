import paho.mqtt.client as mqtt
from Objects import BaseObject


class MQTTClient(BaseObject):
    def __init__(self):
        self.client = mqtt.Client()

    def connect(self):
        q = self.client.connect("localhost", 1883)
        return "Connection to localhost, Quality {i}".format(i=q)

    def init(self):
        pass

    def on_connect(self):
        """
        Logging for debugging
        :return:
        """
        pass

if __name__ == '__main__':

    c = MQTTClient()
    c.name = "Client"
    print(c.get_attribute())
