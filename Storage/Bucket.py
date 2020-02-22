import os

from StorageErrorMessages import AlreadyCreatedError


class Bucket:
    def __init__(self, name):
        self.__name = name
        self.__dir_path = os.path.dirname(__file__)

    @property
    def name(self):
        return self.__name

    def create_bucket(self):
        if self.__check_if_exits():
            raise AlreadyCreatedError("A Bucket with this name is already created. Please use a different name.")
        else:
            os.makedirs(os.path.join(self.__dir_path, self.__name))
            return True

    def __check_if_exits(self):
        return os.path.exists(os.path.join(self.__dir_path, self.__name))

    def put(self, path, data, overwrite=True, append=False):
        file_path = os.path.join(self.__dir_path, self.__name, path)
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        if not overwrite:
            if append:
                with open(file_path, 'a') as file:
                    file.write(data)
                print("File is saved")
            if os.path.isfile(file_path):
                print("File already exits")
        else:
            with open(file_path, 'w') as file:
                file.write(data)
            print("File is saved")

    def get(self, path):
        file_path = os.path.join(self.__dir_path, self.__name, path)
        if not os.path.exists(file_path):
            raise FileNotFoundError()
        else:
            with open(file_path, 'r') as file:
                return file.read()

    def delete(self):
        if input("Please confirm your decision, that you want to delete {b} \n with Y/n".format(b=self.__name)) == "Y":
            os.rmdir(os.path.join(self.__dir_path, self.__name))
            return True
        else:
            return False


if __name__ == '__main__':
    import json

    Bucket = Bucket("Bucket")
    data = json.dumps({"DataPoint1": 1, "DataPoint2": 2, "DataPoint3": 3})
    file_path = 'test/data.json'
    Bucket.put(file_path, data)
    data = Bucket.get(file_path)
    print(data)
    print(json.loads(str(data)))
