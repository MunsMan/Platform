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

    def list_of_endpoints(self):
        endnote = []
        tree_root = self.file["data"]
        return self._recursive_scan(tree_root, "root")

    def _recursive_scan(self, node, key):
        endnode = []
        nnode = node[key]
        print(nnode)
        if nnode["nodes"] == {}:
            print("True")
            return key
        else:
            for nkey in nnode["nodes"].keys():
                endnode.append(self._recursive_scan(nnode["nodes"], nkey))
        return endnode



if __name__ == '__main__':
    config = JSONHandler()
    print(config.list_of_endpoints())

