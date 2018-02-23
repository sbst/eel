import HashMap
import os
import sys
import argparse


def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path with target files")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("path " + args.path + " does not exist")
        return None
    else:
        return args.path


def main():
    os.chdir(get_path())
    hash_map = HashMap.HashMap()
    for filename in os.listdir(os.getcwd()):
        size = os.path.getsize(filename)
        hash_map.process(size, filename)
    return 0


if __name__ == '__main__':
    sys.exit(main())
