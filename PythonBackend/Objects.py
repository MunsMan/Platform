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

    def get_attribute(self):
        att = self.__dict__
        att_json = {}
        for a in att.keys():
            if att[a] is None:
                continue
            else:
                att_json[a] = att[a]
        inspect.getmembers(self)
        return json.dumps(att_json)

    def load_from_json(self, j):
        j = json.loads(j)
        for i in j:
            self.__dict__[i] = j[i]



if __name__ == '__main__':
    FO = BaseObject("BaseSPS")
    j = FO.get_attribute()
