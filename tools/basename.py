import sys


def get_basename(name):
    name_index = len(name) - 1
    while name_index >= 0 and name[name_index] != '/':
        name_index -= 1
    # print(name[name_index + 1:])
    return name[name_index + 1:]


def option_a(argv, delimiter='\n'):
    a_index = argv.index('-a')
    names = argv[a_index+1:]
    result = []
    for name in names:
        basename = get_basename(name)
        result.append(basename)

    if result:
        return delimiter.join(result) + delimiter 
    else:
        return ''


def option_s(argv, delimiter='\n'):
    s_index = argv.index('-s')
    suffix = argv[s_index + 1]
    names = argv[s_index+2:]
    result = []
    for name in names:
        basename = get_basename(name)
        if suffix == basename[-len(suffix):]:
            result.append(basename[:len(basename) - len(suffix)])
        else:
            result.append(basename)
    if result:
        return delimiter.join(result) + delimiter 
    else:
        return ''


if __name__ == "__main__":
    if len(sys.argv) > 1:
        option_found = False
        option_z = False
        if sys.argv[1] == '-z':
            option_z = True
            sys.argv = sys.argv[2:]
        options = [('-a', option_a), ('-s', option_s)]
        for option, option_fn in options:
            if option in sys.argv:
                result = option_fn(sys.argv, '' if option_z else '\n')
                option_found = True
        if not option_found:
            name = sys.argv[1]
            basename = get_basename(name)
            print(basename)
        else:
            print(result)
    else:
        print(f'usage: {sys.argv[0]} NAME')
