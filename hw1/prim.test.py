#!/usr/bin/python
import unittest
from prim import *

def parseFile(fileName):
    with open(filename, 'r') as f:
        return

class PrimTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(0, mstWeight([]))

if __name__ == '__main__':
    unittest.main()
