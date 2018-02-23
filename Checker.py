from hashlib import sha256


def get_hash(hasher, filename, blocksize = 65536):
    with open(filename, "rb") as file:
        block = file.read(blocksize)
        while block:
            hasher.update(block)
            block = file.read(blocksize)
        return hasher.hexdigest()


# Functor for comparison hashes by get_hash
class Checker:
    def __init__(self, target):
        if target == "":
            raise FileNotFoundError("Empty filename to compare")
        self.found = False
        self.target = target
        self.hash = get_hash(sha256(), target)

    def is_not_found(self, filename):
        if not self.found:
            if get_hash(sha256(), filename) == self.hash:
                print(filename + " " + self.target)
                self.found = True
                return False

        return True
