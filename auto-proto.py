import os
import sys
import os.path
from os import path

def search_for_prototypes(paths):
    inside = open(paths, "r")
    prev_line = ""
    proto_h = open("include/proto.h", "a")
    for lines in inside:
        if lines[0] == '{':
            proto_h.write(prev_line)
        prev_line = lines
    proto_h.close()
    inside.close()

def browse_dir(directory, paths):
    for elements in directory:
        pth = paths + "/" + elements
        if path.isdir(pth):
            browse_dir(os.listdir(pth), pth)
        else:
            if ".c" in elements:
                search_for_prototypes(pth)

def main():
    directory = os.listdir(".")
    in_file = ""
    created = 0
    pth = os.path.expanduser('~') + "/.auto-proto-script/proto_file.txt"
    for elmnt in directory:
        if "include" in elmnt and path.isdir(elmnt):
            created += 1
            proto_h = open(pth, "r")
            for lines in proto_h:
                in_file += lines
            proto_h.close()
            fd = open("include/proto.h", "w")
            fd.write(in_file)
            fd.close()
    if created == 0:
        print("No include folder found")
        return
    else:
        browse_dir(directory, ".")
        inside = open("include/proto.h", "a")
        inside.write("\n#endif /* PROTO_H_ */\n")


main()
