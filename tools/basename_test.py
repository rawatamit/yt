import pytest
from basename3 import get_basename, option_a, option_s 

def f(x):
    return x + 1

def test_f_1():
    assert f(3) == 4
    assert f(4) == 5

def test_get_basename():
    assert get_basename('/') == ''
    assert get_basename('') == ''
    assert get_basename('sort') == 'sort'
    assert get_basename('/sort') == 'sort'
    assert get_basename('/usr/sort') == 'sort'
    assert get_basename('/usr/sort.h') == 'sort.h'

def test_option_a(capsys):
    # no names
    argv1 = ['-a']
    option_a(argv1)
    captured1 = capsys.readouterr()
    assert captured1.out == ''

    # one name
    argv2 = ['-a', 'sort']
    option_a(argv2)
    captured1 = capsys.readouterr()
    assert captured1.out == 'sort\n'

    # multiple names
    argv3 = ['-a', 'sort', '/usr/stdio.h']
    option_a(argv3)
    captured1 = capsys.readouterr()
    assert captured1.out == 'sort\nstdio.h\n'

def test_option_s(capsys):
    # no names
    argv1 = ['-s']
    with pytest.raises(IndexError):
        option_s(argv1)

    # only suffix
    argv2 = ['-s', '.h']
    option_s(argv2)
    captured1 = capsys.readouterr()
    assert captured1.out == ''

    # suffix + name
    argv2 = ['-s', '.h', 'stdio.h', '/usr/stdio.h', 'cmp']
    option_s(argv2)
    captured1 = capsys.readouterr()
    assert captured1.out == 'stdio\nstdio\ncmp\n'
