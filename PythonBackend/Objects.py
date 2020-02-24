from hashlib import md5
import time
import json
import inspect
from Extensions import MQTTClient
from typing import Dict, List


class BaseObject:
    def __init__(self, name=None):
        self.__data = None
        self.__address = None
        self.name = name
        self.description = None
        self.id = self.__create_id_()
        self.__str__ = self.__get_classname()
        self.__bigger_node = None
        self.__smaller_nodes = {}
        self.__possible_data_sources = {"node": self.__get_data_from_node, "mqtt": self.__get_data_from_mqtt}
        self.__listener = []

    @classmethod
    def __get_classname(cls) -> str:
        return cls.__name__

    def get_name(self) -> str:
        if self.name is None:
            return self.__get_classname()
        else:
            return self.name

    def set_description(self, text) -> None:
        self.description = str(text)
        self.__str__ = str(text)

    def __create_id_(self) -> str:
        m = md5()
        m.update(str(time.time()).encode())
        name = self.get_name()
        return name + "<" + m.hexdigest() + ">"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
        self.__on_change_handler(data)

    def subscribe_to_data(self, handler):
        self.__listener.append(handler)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @address.setter
    def address(self, node):
        if self.bigger_node is None:
            self.__bigger_node = node
        else:
            self.change_bigger_node(node)

    @property
    def bigger_node(self):
        return self.__bigger_node

    @bigger_node.setter
    def bigger_node(self, node):
        node_id = node.id
        if self.bigger_node is None:
            self.__bigger_node = node_id
        else:
            self.change_bigger_node(node_id)

    def change_bigger_node(self, node_id):
        ui = input("Are you sure to change the hierarchy? (y/n)")
        if ui is "y":
            self.__bigger_node = None
            self.address = node_id
        elif ui is "n":
            pass
        else:
            print("Wrong Input, try again.")

    @property
    def smaller_node(self) -> list:
        return list(self.__smaller_nodes.keys())

    @smaller_node.setter
    def smaller_node(self, node) -> None:
        node_id = node.id
        self.__smaller_nodes[node_id] = node

    def smaller_node_del(self, node) -> None:
        node_id = node.id
        nodes = self.smaller_node
        if node_id in self.__smaller_nodes.keys():
            self.smaller_node.pop(node_id)

    def get_attribute(self) -> json:
        att = self.__dict__
        att_json = {}
        for a in att.keys():
            if att[a] is None:
                continue
            else:
                att_json[a] = str(att[a])
        print(att_json)
        return json.dumps(att_json)

    def load_from_json(self, j):
        j = json.loads(j)
        for i in j:
            self.__dict__[i] = j[i]

    def get_source(self, source: str, type: str):
        """
            :param source: specifying the node or topic
            :param type: information about the data source, for example MQTT or reference of a different node
        """
        if not type.lower() in self.__possible_data_sources.keys():
            print("specified type of data source is not supported")
            return False
        else:
            source_handler = self.__possible_data_sources[type]
            source_handler = source_handler(source)

    def __data_change_listener(self, data_source, type):
        pass

    def __get_data_from_node(self, source):
        node = self.children_search(source[0])
        if source[1] is None:
            node.subscribe_to_data(self._base_node_handler)
        else:
            node.subscribe_to_data(source[1])

    def _base_node_handler(self, data):
        print(data)
        self.data = data

    def __get_data_from_mqtt(self, source):
        mqtt_client = MQTTClient(device_name=source[0])
        mqtt_client.connect()
        mqtt_client.subscriber(topic=source[1])
        mqtt_client.client.on_message = self.__data_change_listener
        mqtt_client.init()

    def children_search(self, child):
        if child in self.smaller_node:
            return self.__smaller_nodes[child]
        else:
            for smaller_node in self.__smaller_nodes.values():
                ans = smaller_node.children_search(child)
                if ans is not None:
                    return ans

    def __on_change_handler(self, data):
        if self.__listener is None:
            return
        else:
            for listener in self.__listener:
                listener(data)


if __name__ == '__main__':
    Aquarium = BaseObject("Aquarium")
    Pumpe = BaseObject("Pumpe")
    Motor = BaseObject("Motor")
    Aquarium.description = "Ich bin das Grundobjekt"
    Pumpe.description = "Ich bin die Pumpe"
    Motor.description = "Ich bin das dritte Objekt und gehöre unter die Pumpe"
    Aquarium.smaller_node = Pumpe
    Pumpe.bigger_node = Aquarium
    Pumpe.smaller_node = Motor
    Motor.bigger_node = Pumpe

    source = [Pumpe.id, None]
    Aquarium.get_source(source, 'node')
    Pumpe.data = 1
    print("Aquarium Data:", Aquarium.data)
