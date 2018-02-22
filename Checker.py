from hashlib import sha256


def get_hash(hasher, filename, blocksize=65536):
    with open(filename, "rb") as file:
        block = file.read(blocksize)
        while block:
            hasher.update(block)
            block = file.read(blocksize)
        return hasher.hexdigest()


def compare(filename1, filename2):
    return get_hash(sha256(), filename1) == get_hash(sha256(), filename2)