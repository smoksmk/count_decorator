import unittest

from count_decorator import Counter


class TestStringMethods(unittest.TestCase):

    def test_counter(self):
        count_decorator = Counter()

        @count_decorator
        def counter():
            pass

        for i in range(10):
            counter()
        self.assertTrue(count_decorator.count == 10)

    def test_with_params(self):
        count_decorator = Counter()

        @count_decorator
        def counter(*args, **kwargs):
            return args, kwargs

        arg, kwarg = counter(1, param=1)
        self.assertTrue(count_decorator.count == 1)
        self.assertTrue(arg == (1,))
        self.assertTrue(kwarg == {'param': 1})


if __name__ == '__main__':
    unittest.main(verbosity=2)