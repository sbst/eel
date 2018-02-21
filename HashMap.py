class HashMap:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data.update({key: value})


    def get(self, key):
        return self.data.get(key)


    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, value):
        self.put(key, value)
