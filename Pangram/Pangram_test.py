import unittest
from Pangram.Pangram_function import pangram_check


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(pangram_check('The quick brown fox jumps over the lazy dog'), True)


if __name__ == '__main__':
    unittest.main()
