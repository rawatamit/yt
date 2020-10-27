import sys


def get_basename(name):
    name_index = len(name) - 1
    while name_index >= 0 and name[name_index] != '/':
        name_index -= 1
    # print(name[name_index + 1:])
    return name[name_index + 1:]


def option_a(argv):
    a_index = argv.index('-a')
    names = argv[a_index+1:]
    for name in names:
        basename = get_basename(name)
        print(basename)


def option_s(argv):
    s_index = argv.index('-s')
    suffix = argv[s_index + 1]
    names = argv[s_index+2:]
    for name in names:
        basename = get_basename(name)
        if suffix == basename[-len(suffix):]:
            print(basename[:len(basename) - len(suffix)])
        else:
            print(basename)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        option_found = False
        options = [('-a', option_a), ('-s', option_s)]
        for option, option_fn in options:
            if option in sys.argv:
                option_fn(sys.argv)
                option_found = True
        if not option_found:
            name = sys.argv[1]
            basename = get_basename(name)
            print(basename)
    else:
        print(f'usage: {sys.argv[0]} NAME')
