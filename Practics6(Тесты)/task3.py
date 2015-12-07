import unittest
import lib
class LibTest(unittest.TestCase):
    def test_palindrome_s_arg(self):
        self.assertEqual(lib.palindrome('ABCCBA'), 1)
        self.assertEqual(lib.palindrome('ABC'), 0)
        self.assertEqual(lib.palindrome('A'),1)  
unittest.main(verbosity=2)
