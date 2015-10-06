import unittest
import lib
import math
class LibTest(unittest.TestCase):
    def test_sin_arg(self):
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin((math.pi)/2), 1)
        self.assertEqual(lib.sin((math.pi)/(-2)),-1)
        self.assertEqual(lib.sin((math.pi)*(-1)),0)   
unittest.main(verbosity=2)
