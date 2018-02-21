import HashMap
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path with target files")
    args = parser.parse_args()

    if (os.path.exists(args.path)) == False:
        print("path " + args.path + " does not exist")
        return 1
    else:
        path = args.path

    map = HashMap.HashMap()
    for filename in os.listdir(path):
        size = os.path.getsize(path + filename)
        value = map.get(size)
        if value == None:
            map.put(size, filename)
        else:
            print(map.data.pop(size) + " " + filename)

    return 0


if __name__ == '__main__':
    os._exit(main())
