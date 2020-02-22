import os

from Bucket import Bucket
# Errors
from StorageErrorMessages import ErrorWillCreatingBucket
from StorageManagementFile import StorageManagementFile


class StorageManager:
    def __init__(self):
        self.__bucket_list = {}
        self.__bucket_dir = os.path.dirname(__file__)
        self.__file_name = ".StorageManagement.json"
        self.__file_path = os.path.join(self.__bucket_dir, self.__file_name)
        self.__smf = StorageManagementFile(self.__bucket_dir)
        self.__smf.init()
        self.sync_storage()
        self.load_buckets()

    @property
    def bucket_amount(self):
        return self.__smf.bucket_amount()

    def sync_storage(self):
        smf_buckets = self.__smf.buckets()
        for bucket in smf_buckets:
            if not os.path.exists(os.path.join(self.__bucket_dir, bucket)):
                print("Sync Error")

    def create_new_bucket(self, name, size, access):
        smf_status = self.__smf.add_bucket(name, size, access)
        bucket = Bucket(name)
        self.__bucket_list[bucket.name] = bucket
        bucket_status = bucket.create_bucket()
        if not (smf_status and bucket_status):
            ErrorWillCreatingBucket(message="Could not create the wanted Bucket", data=(smf_status, bucket_status))
        return True

    def list_buckets(self):
        return self.__smf.buckets()

    def delete_all_buckets(self):
        for bucket in self.__bucket_list:
            self.__bucket_list[bucket].delete()
            self.__smf.rm_bucket(bucket)

    def load_buckets(self):
        for bucket in self.list_buckets():
            self.__bucket_list[bucket] = Bucket(bucket)

    def put(self, data, bucket: str, path: str, overwrite: bool = True, append: bool = False):
        if bucket in self.__smf.buckets():
            sel_bucket = self.__bucket_list[bucket]
            sel_bucket.put(path, data, overwrite=overwrite, append=append)


if __name__ == '__main__':
    Manager = StorageManager()
    Manager.delete_all_buckets()
    Manager.create_new_bucket("Bucket1", (1, "gb"), [True, True, True, False])
    Manager.create_new_bucket("Bucket2", (1, "gb"), [True, True, True, False])

    print(Manager.bucket_amount)
