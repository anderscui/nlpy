# coding=utf-8
from common.persistence import to_pickle, from_pickle, to_json, from_json


def test_pickle_simple_object():
    i = 100
    fpath = './tests/int.pkl'
    to_pickle(i, fpath)

    from_file = from_pickle(fpath)
    assert i == from_file


def test_pickle_complex_object():
    d = {'u': u'中文',
         's': 'hello',
         'i': 100,
         'l': [1, [2, 3]]}

    fpath = './tests/complex.pkl'
    to_pickle(d, fpath)

    from_file = from_pickle(fpath)
    assert isinstance(from_file['u'], unicode)
    assert isinstance(from_file['s'], str)
    assert isinstance(from_file['i'], int)
    assert isinstance(from_file['l'], list)

    assert from_file == d


def test_json_simple_object():
    i = 100
    fpath = './tests/int.json'
    to_json(i, fpath)

    from_file = from_json(fpath)
    assert i == from_file


def test_json_complex_object():
    d = {'u': u'中文',
         's': 'hello',
         'i': 100,
         'l': [1, [2, 3]]}

    fpath = './tests/complex.json'
    to_json(d, fpath)

    from_file = from_json(fpath)
    assert isinstance(from_file['u'], unicode)

    # UNICODE...
    assert isinstance(from_file['s'], unicode)

    assert isinstance(from_file['i'], int)
    assert isinstance(from_file['l'], list)

    assert from_file == d


if __name__ == '__main__':
    test_json_complex_object()