import Checker


# Structure for {size : [filenames]} data collection and access
class HashMap:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def process(self, key, value):
        if self.data.get(key) is None:
            self.data.update({key: [value]})
        else:
            self.__check(key, value)

    # Compare data with already existing values
    # If found in checker is false - original file differs from all others and will be collected
    def __check(self, key, value):
        func = Checker.Checker(value)
        updated = [x for x in self.data[key] if func.is_not_found(x)]
        if not func.found:
            updated.append(value)

        if not updated:
            self.data.pop(key)
        else:
            self.data[key] = updated