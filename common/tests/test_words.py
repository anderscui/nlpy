from common.words import edit_dist


def test_edit_dist():

    s1 = ''
    s2 = 'a'
    assert edit_dist(s1, s2) == 1

    s1 = ''
    s2 = 'abc'
    assert edit_dist(s1, s2) == 3

    s1 = 'a'
    s2 = 'a'
    assert edit_dist(s1, s2) == 0

    s1 = 'a'
    s2 = 'b'
    assert edit_dist(s1, s2) == 2

    s1 = 'intention'
    s2 = 'execution'
    assert edit_dist(s1, s2) == 8

    s1 = 'a'
    s2 = 'b'
    assert edit_dist(s1, s2, 1) == 1

    s1 = 'intention'
    s2 = 'execution'
    print(edit_dist(s1, s2, 1))
    assert edit_dist(s1, s2, 1) == 5