#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys.path.append("/path/to/hidden_4_module_directory")
    import hidden_4
    for s in dir(hidden_4):
        if s[:2] != "__":
            print("{:s}".format(s))
