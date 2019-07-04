#!/usr/bin/python3
import getopt
import sys
import os
from os.path import isfile, join

version = '1.0'
verbose = False
output_filename = 'default.out'

folder_path = os.getcwd()
namespace = None


def find_start_in_lines(filename, file_lines):
    if not filename.startswith("rtwtypes"):
        for index, line in reversed(list(enumerate(file_lines))):
            if line.startswith("#include"):
                return index
    else:
        return -1


def find_end_in_lines(filename, file_lines):
    if not filename.startswith("rtwtypes") and filename.endswith("h"):
        for index, line in reversed(list(enumerate(file_lines))):
            if line.startswith("#endif"):
                return index
    elif filename.endswith("cpp"):
        return len(file_lines) - 1
    else:
        return -1


def convert_files():
    global folder_path, namespace
    files = [f for f in os.listdir(folder_path) if
             isfile(join(folder_path, f)) and (f.endswith('cpp') or f.endswith('h'))]
    if len(files) == 0:
        print("There are no files to convert in this directory")
        return
    for f in files:
        file_lines = []
        with open(folder_path + '/' + f, 'r') as file:
            file_lines = file.readlines()
            if len(file_lines) == 0:
                print("Empty file: ", folder_path + '/' + f)
                continue
            insert_line = find_start_in_lines(f, file_lines)
            end_line = find_end_in_lines(f, file_lines)
            if insert_line < 0 or end_line < 0:
                print("Aborting for " + folder_path + '/' + f)
                continue

            file_lines.insert(insert_line + 1, "namespace " + namespace + " {")
            file_lines.insert(end_line, "}")
        with open(folder_path + '/' + f, "w") as file:
            output = "".join(file_lines)
            print("Saving changes to " + folder_path + '/' + f)
            file.write(output)


def main():
    global namespace, folder_path
    options, remainder = getopt.getopt(sys.argv[1:], 'dn:h', ['help', 'namespace=', 'dir='])
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print("Matlab to C++ Namespace adder")
            print("Description: \n"
                  "The program adds namespace clauses in .cpp and .h files.\n"
                  "Executing this program is needed for each exported Matlab function.")
            print("Usage:")
            print("\t --namespace <name> \t Pass name of namespace. Required.")
            print("\t --dir <path> \t \t Select folder with the exported function."
                  " If this argument is omitted, current directory is selected")
            print("Example:")
            print("matcppnamespaces --namespace ltpn --dir ./ltp")
            return
        elif opt in ('-d', '--dir'):
            folder_path = os.path.abspath(arg)
        elif opt in ('-n', '--namespace'):
            namespace = arg

    if namespace is None:
        print("Namespace is required! Pass parameter -n or --namespace")
    else:
        convert_files()


if __name__ == "__main__":
    main()
