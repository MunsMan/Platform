import json
import os


class JSONHandler:
    def __init__(self, name=None, path=None):
        self.name = self._get_name(name)
        self.path = self._get_path(path, self.name)
        self.file = self._read()

    @staticmethod
    def _get_name(name):
        if name is None:
            return "config.json"
        elif ".json" not in name:
            return name + ".json"

    @staticmethod
    def _get_path(path, name):
        if path is None:
            return os.path.join(os.path.dirname(__file__), name)
        elif name not in path:
            return os.path.join(path, name)

    def _read(self):
        with open(self.path) as file:
            json_file = json.load(file)
        return json_file

    def display(self):
        return self.file

    def change_file(self, file):
        self.file = file

    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.file, file)

    def list_of_tree(self):
        tree_root = self.file["data"]
        return self._recursive_scan(tree_root, "root")

    def _recursive_scan(self, node, key):
        endnode = []
        nnode = node[key]
        if nnode["nodes"] == {}:
            endnode.append(key)
            return endnode
        else:
            endnode.append(key)
            for nkey in nnode["nodes"].keys():
                endnode.append(self._recursive_scan(nnode["nodes"], nkey))
        return endnode

    def create_object_model(self, base_object):
        root = self.file["data"]
        return self._recursive_object_model(base_object, root, "root")

    def _recursive_object_model(self, base_object, node, key):
        new_obj = base_object(key)
        objects = [new_obj]
        if 'description' in node[key].keys():
            new_obj.description = node[key]["description"]
        if node[key]['nodes'] != {}:
            for nkey in node[key]['nodes'].keys():
                nnode = self._recursive_object_model(base_object, node[key]['nodes'], nkey)
                new_obj.smaller_node = nnode[0]
                objects.append(nnode)
        return objects


class SpecialPrint:
    def __init__(self):
        pass

    def print_tree(self, tree):
        level = 0
        self._re_print(tree, level)

    def _re_print(self, node, level):
        level += 1
        self.__p_arm(node[0], level)
        if len(node) > 2:
            for n in node[1:]:
                self._re_print(n, level)
        elif len(node) == 1:
            return True
        else:
            self._re_print(node[1], level)

    @staticmethod
    def __p_arm(name, level):
        print("-" * level, name)


def cal_topic(tree, name, node):
    pass


if __name__ == '__main__':
    config = JSONHandler()
    print(config.list_of_tree())

