import os
import sys
import os.path
from os import path

def search_for_prototypes(paths):
    init = open(paths, "r")
    inside = init.read().split("\n")
    prev_line = ""
    proto_h = open("include/proto.h", "a")
    for id in range(1, len(inside) - 1, 1):
        if inside[id].replace("\n", "").replace(" ", "").replace("\t", "") == "{" and inside[id][0] == '{':
            i = id - 1
            tot = []
            while ("(" not in inside[i + 1]):
                tot.append(inside[i] + ("\n" if i < id - 1 else ""))
                i -= 1
            tot.reverse()
            print(tot)
            tot = ''.join(tot)
            tot += ";\n"
            proto_h.write(tot)
    proto_h.close()
    init.close()

def browse_dir(directory, paths):
    for elements in directory:
        pth = paths + "/" + elements
        if path.isdir(pth):
            browse_dir(os.listdir(pth), pth)
        else:
            if ".c" in elements and not("bonus/" in pth) and not("tests" in pth):
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
