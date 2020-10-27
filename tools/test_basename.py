import pytest
from basename import get_basename, option_a, option_s


def test_get_basename():
    assert get_basename('') == ''
    assert get_basename('/') == ''
    assert get_basename('/sort') == 'sort'
    assert get_basename('sort') == 'sort'
    assert get_basename('/usr/sort') == 'sort'


def test_option_a():
    argv1 = ['-a']
    result = option_a(argv1)
    assert result == ''

    argv2 = ['-a', '/usr/cmp']
    result = option_a(argv2)
    assert result == 'cmp\n'

    argv3 = ['-a', '/usr/cmp', 'cmp']
    result = option_a(argv3)
    assert result == 'cmp\ncmp\n'

    argv4 = ['-a', 'sort']
    result = option_a(argv4, delimiter='')
    assert result == 'sort'


def test_option_s(capsys):
    argv1 = ['-s']

    with pytest.raises(IndexError):
        option_s(argv1)
    
    argv2 = ['-s', '.h']
    result = option_s(argv2)
    assert result == ''

    argv3 = ['-s', '.h', '/usr/sort', 'cmp', '/usr/stdio.h', '/usr/stdio.c']
    result = option_s(argv3)
    assert result == 'sort\ncmp\nstdio\nstdio.c\n'

    argv4 = ['-s', '.h', 'stdio.h', 'stdio.c']
    result = option_s(argv4, delimiter='')
    assert result == 'stdiostdio.c'
