import os
import time


class Log:
    def __init__(self, name):
        self.id = name
        self.log_name = self.get_name()
        self.create_log()

    def get_name(self):
        return "Log-<"+str(self.id)+">.txt"

    def __file_pos(self):
        path = os.path.dirname(__file__)
        filepath = os.path.join(path, "..", "Logs", self.log_name)
        return filepath

    def create_log(self):
        f = open(self.__file_pos(), 'w+')
        f.write("Log of {n}: \n".format(n=self.id))
        f.close()

    def log_post(self, post):
        log_head = str(time.asctime()) + ": " + str(post)
        f = open(self.__file_pos(), "a")
        f.write(log_head)
        f.close()


if __name__ == '__main__':
    TestLog = Log("Test")
    TestLog.log_post("Connection found")
