import os
import time

class Log:
    def __init__(self, id):
        self.id = id
        self.log_name = self.get_name

    def get_name(self):
        return "log"+"<"+str(self.id)+">.txt"

    def create_log(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, "log")
        f = open(str(self.log_name), 'w+')
        f.write("Log of {n}: \n".format(n=self.id))

    @staticmethod
    def log_post(post):
        log_head = "log " + str(time.asctime()) + ": " + str(post)
        return log_head



