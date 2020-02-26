from Objects import BaseObject
from Functions import JSONHandler
import json
import os


class ObjectManager:
    def __init__(self):
        self.nodes = {}
        self.__file_name = ".IotManager.json"
        self.__file_path = os.path.join(os.path.dirname(__file__), self.__file_name)

    def init(self):
        pass

    def create_node(self, name, parent=None, children=None):

        obj = BaseObject(name)
        node = {
            "name": obj.name,
            "id": obj.id,
            "obj": obj,
            "parent": parent,
            "children": children
        }
        self.nodes[name] = node

    def add_parent(self, name: str, parent_name: str):
        node = self.nodes[name]
        node.bigger_node(self.nodes[parent_name])

    def add_child(self, name: str, child_name: str):
        node = self.nodes[name]
        node.smaller_node(self.nodes[child_name])

    def get_node(self, name):
        if name in self.nodes:
            return self.nodes[name]
        else:
            return False

    def load_manager(self, data):
        pass

    def save_manager(self):
        data = {
            "nodes": self.nodes
        }
        json.dump(data, )


if __name__ == '__main__':
    data = {
        "hierarchy": {
            "root": {
                "name": "Aquarium",
                "id": "12",
                "obj": "node",
                "parent": "root",
                "children": {
                    "Pumpe": {
                        "name": "Aquarium",
                        "id": "21",
                        "obj": "node",
                        "parent": "Aquarium",
                        "children": {
                            "Motor": {
                                "name": "Aquarium",
                                "id": "15",
                                "obj": "node",
                                "parent": "Pumpe",
                                "children": {}
                            }
                        }
                    },
                    "Sensor": {
                        "name": "Aquarium",
                        "id": "17",
                        "obj": "node",
                        "parent": "Aquarium",
                        "children": {},
                    }
                }
            }
        }
    }
    Manager = ObjectManager()
    Manager.load_data(data["hierarchy"])
    node = {
        "name": "Durchflussmesser",
        "id": "34",
        "obj": "node",
        "parent": "Aquarium",
        "children": {}
    }
    Manager.create_node(node["name"], node)
