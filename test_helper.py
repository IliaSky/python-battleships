import unittest


def must_be_true(expression):
    return unittest.TestCase().assertTrue(expression)


def must_be_false(expression):
    return unittest.TestCase().assertFalse(expression)


def must_be_equal(expected, expression):
    return unittest.TestCase().assertTrue(expected, expression)


def must_raise(error, *args):
    return unittest.TestCase().assertRaises(error, *args)
