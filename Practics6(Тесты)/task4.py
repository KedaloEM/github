import unittest
import lib
class LibTest(unittest.TestCase):
    def test_prime_arg(self):
        self.assertEqual(lib.prime(4), 0)
        self.assertEqual(lib.prime(23), 1)
        self.assertEqual(lib.prime(0),0)
        self.assertEqual(lib.prime(-15),0)
unittest.main(verbosity=2)
