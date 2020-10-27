import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
        name_index = len(name) - 1
        while name_index >= 0 and name[name_index] != '/':
            name_index -= 1
        basename = name[name_index+1:]
        print(basename)
    else:
        print(f'usage: {sys.argv[0]} NAME')
