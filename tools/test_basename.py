import pytest
from basename import get_basename, option_a, option_s


def test_get_basename():
    assert get_basename('') == ''
    assert get_basename('/') == ''
    assert get_basename('/sort') == 'sort'
    assert get_basename('sort') == 'sort'
    assert get_basename('/usr/sort') == 'sort'


def test_option_a(capsys):
    argv1 = ['-a']
    option_a(argv1)
    captured = capsys.readouterr()
    assert captured.out == ''

    argv2 = ['-a', '/usr/cmp']
    option_a(argv2)
    captured = capsys.readouterr()
    assert captured.out == 'cmp\n'

    argv3 = ['-a', '/usr/cmp', 'cmp']
    option_a(argv3)
    captured = capsys.readouterr()
    assert captured.out == 'cmp\ncmp\n'


def test_option_s(capsys):
    argv1 = ['-s']

    with pytest.raises(IndexError):
        option_s(argv1)
    
    argv2 = ['-s', '.h']
    option_s(argv2)
    captured = capsys.readouterr()
    assert captured.out == ''

    argv3 = ['-s', '.h', '/usr/sort', 'cmp', '/usr/stdio.h', '/usr/stdio.c']
    option_s(argv3)
    captured = capsys.readouterr()
    assert captured.out == 'sort\ncmp\nstdio\nstdio.c\n'
