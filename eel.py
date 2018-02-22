import HashMap
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
        map = HashMap.HashMap(path)
        for filename in os.listdir(path):
            size = os.path.getsize(os.path.join(path, filename))
            map.process(size, filename)
        return 0
    else:
        return 1


if __name__ == '__main__':
    os._exit(main())
