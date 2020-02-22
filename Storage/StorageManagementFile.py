import json
import os


class StorageManagementFile:
    def __init__(self, dir_path):
        self.__dir = dir_path
        self.__name = ".StorageManagement.json"
        self.__file_path = os.path.join(self.__dir, self.__name)
        self.__smf = None

    def init(self):
        if not self.__look_this_dir():
            self.__smf = {
                "settings":
                    {
                        "allocated": {
                            "size": 10,
                            "unit": "gb"
                        },
                        "used": {
                            "size": 0,
                            "unit": "b"
                        }
                    },
                "buckets": [],
                "bucket_pos": {}
            }
            self.__update_smf()
        else:
            self.__load_file()

    def create_new_file(self):
        pass

    def __look_this_dir(self):
        if not os.path.exists(self.__file_path):
            return False
        else:
            return True

    def look_there(self, path):
        if not os.path.exists(os.path.join(path, self.__name)):
            return False
        else:
            return True

    def full_search(self):
        # ToDo: build a search for every directory on the given machine. Recursive
        pass

    def __load_file(self):
        if self.__look_this_dir():
            with open(self.__file_path, 'r') as file:
                self.__smf = json.loads(file.read())

    def size(self):
        # ToDo: Calculate the file_size
        pass

    def __update_smf(self):
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__smf))
        return True
        # CouldNotUpdateSMF("Error will updating", self.__smf)

    def add_bucket(self, name: str, size: (int, str), access: list):
        size, unit = size
        bucket = {
            "name": name,
            "allocated": {
                "size": size,
                "unit": unit
            },
            "used": {
                "size": 0,
                "unit": "b"
            },
            "access": {
                "read": access[0],
                "write": access[1],
                "public": access[2],
                "encoded": access[3],
                "user": []
            },
            "key": None
        }
        bucket_pos = self.bucket_amount()
        self.__smf["bucket_pos"][name] = bucket_pos
        self.__smf["buckets"].append(bucket)
        return self.__update_smf()

    def bucket_amount(self):
        return self.__smf["buckets"].__len__()

    def buckets(self):
        return list(self.__smf["bucket_pos"].keys())

    def rm_bucket(self, name):
        pos = self.__smf["bucket_pos"][name]
        self.__smf["buckets"].pop(pos)
        self.sync_pos()
        return True

    def sync_pos(self):
        i = 0
        self.__smf['bucket_pos'] = {}
        for bucket in self.__smf["buckets"]:
            name = bucket['name']
            self.__smf['bucket_pos'][name] = i
            i += 1
