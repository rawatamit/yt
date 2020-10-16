import sys

# we differ in this circumstance
# -z is not supported
# python basename4.py -a -s .h /usr/stdio.h /cmp
# -a is provided we still need to scan whether 
# other arguments are provided
# first fix more than one option
# second return result as list, add a loop to print
# add end to end basenames

class UnknownOptionException(Exception):
    pass


def get_basename(name):
    name_index = len(name) - 1
    while name_index >= 0 and name[name_index] != '/':
        name_index -= 1
    # print(name[name_index + 1:])
    return name[name_index + 1:]


def option_a(argv):
    a_index = argv.index('-a')
    names = argv[a_index+1:]
    result = []
    for name in names:
        basename = get_basename(name)
        result.append(basename)
    return result


def option_s(argv):
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
    return result


def option_z(argv):
    if len(argv) == 2:
        return []
    elif argv[2] == '-a':
        result = option_a(argv[2:])
        return [''.join(result)]
    elif argv[2] == '-s':
        result = option_s(argv[2:])
        return [''.join(result)]
    else:
        raise UnknownOptionException


if __name__ == "__main__":
    if len(sys.argv) > 1:
        option_found = False
        options = [('-a', option_a), ('-s', option_s), ('-z', option_z)]
        for option, option_fn in options:
            if option in sys.argv:
                result = option_fn(sys.argv)
                option_found = True
                break
        if not option_found:
            name = sys.argv[1]
            basename = get_basename(name)
            print(basename)
        else:
            for name in result:
                print(name)
    else:
        print(f'usage: {sys.argv[0]} NAME')
