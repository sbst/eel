import HashMap
import Checker
import os
import argparse

def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path with target files")
    args = parser.parse_args()

    if (os.path.exists(args.path)) == False:
        print("path " + args.path + " does not exist")
        return None
    else:
        return args.path


def main():
    path = get_path()
    if path != None:
        map = HashMap.HashMap()
        for filename in os.listdir(path):
            full_filename = os.path.join(path + filename)
            size = os.path.getsize(full_filename)
            value = map.get(size)
            if value == None:
                map.put(size, filename)
            else:
                if Checker.compare(full_filename, os.path.join(path + value)):
                    print(map.data.pop(size) + " " + filename)
        return 0
    else:
        return 1


if __name__ == '__main__':
    os._exit(main())
