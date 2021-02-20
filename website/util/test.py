import unittest
from base62 import base62_encode, base62_decode


class Base62Test(unittest.TestCase):
    """ unit test"""

    def test_base62(self):
        self.assertEqual(base62_encode(100), '1C')
        self.assertEqual(base62_encode(999999999), '15FTGf')
        self.assertEqual(base62_decode('dtvd3o'), 12345678910)


if __name__ == '__main__':
    unittest.main()
