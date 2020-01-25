from hashlib import md5
import time
import json
import inspect


class BaseObject:
    def __init__(self, name=None):
        self.__data = None
        self.__address = None
        self.name = name
        self.description = None
        self.id = self.__create_id_()
        self.__str__ = self.__get_classname()
        self.__bigger_node = None
        self.__smaller_nodes = None

    @classmethod
    def __get_classname(cls):
        return cls.__name__

    def get_name(self):
        if self.name is None:
            return self.__get_classname()
        else:
            return self.name

    def set_description(self, text):
        self.description = str(text)
        self.__str__ = str(text)

    def __create_id_(self):
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
    def smaller_node(self):
        return self.__smaller_nodes

    @smaller_node.setter
    def smaller_node(self, node):
        node_id = node.id
        if self.__smaller_nodes is None:
            self.__smaller_nodes = [node_id]
        else:
            self.__smaller_nodes.append(node_id)

    def smaller_node_del(self, node):
        node_id = node.id
        nodes = self.smaller_node
        for i in range(len(self.__smaller_nodes)):
            if nodes[i] is node_id:
                self.__smaller_nodes.pop(i)
            else:
                continue

    def get_attribute(self):
        att = self.__dict__
        att_json = {}
        for a in att.keys():
            if att[a] is None:
                continue
            else:
                att_json[a] = att[a]
        return json.dumps(att_json)

    def load_from_json(self, j):
        j = json.loads(j)
        for i in j:
            self.__dict__[i] = j[i]


if __name__ == '__main__':
    FO = BaseObject("BaseSPS")
    SO = BaseObject("SSPS")
    SO.bigger_node = FO
    FO.smaller_node = SO
    print(FO.smaller_node)
    print(SO.bigger_node)
    print(FO.get_attribute())
    print(SO.get_attribute())
