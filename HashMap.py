import Checker
from os.path import join

class HashMap:
    def __init__(self, path):
        self.data = {}
        self.path = path

    def get(self, key):
        return self.data.get(key)

    def process(self, key, input):
        value = self.data.get(key)
        if value == None:
            self.data.update({key: input})
        else:
            if Checker.compare(join(self.path, input), join(self.path, value)):
                print(self.data.pop(key) + " " + input)
