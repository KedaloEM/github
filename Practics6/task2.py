import unittest
import lib
class LibTest(unittest.TestCase):
    def test_even_chet_arg(self):
        self.assertEqual(lib.even(4), 1)
        self.assertEqual(lib.even(0), 1)
        self.assertEqual(lib.even(-2),1)
    def test_even_nechet(self):
        self.assertEqual(lib.factorial(1),0)
        self.assertEqual(lib.factorial(-1),0)
unittest.main(verbosity=2)

