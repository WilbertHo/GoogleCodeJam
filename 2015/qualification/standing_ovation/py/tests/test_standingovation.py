from nose.tools import eq_


def test_calculate_minimum_friends():
    from standingovation import calculate_minimum_friends
    eq_(calculate_minimum_friends(4, [1, 1, 1, 1, 1]), 0)
    eq_(calculate_minimum_friends(1, [0, 9]), 1)
    eq_(calculate_minimum_friends(5, [1, 1, 0, 0, 1, 1]), 2)
    eq_(calculate_minimum_friends(0, [1]), 0)
