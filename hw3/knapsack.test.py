#!/usr/bin/python

import unittest
from knapsack import *

def loadFromFile(filename):
    with open(filename, 'r') as fh:
        header = fh.readline().split()
        knapsackSize = int(header[0])
        lines = map(lambda x: x.split(), fh.readlines())
    items = map(lambda x: (int(x[0]), int(x[1])), lines)
    return knapsackSize, items

class TestLoader(unittest.TestCase):
    def test_load(self):
        knapsackSize, items = loadFromFile('knapsack1.txt')
        self.assertEqual(10000, knapsackSize)
        self.assertEqual(100, len(items))

class Problem1(unittest.TestCase):
    def test_hi(self):
        return

if __name__ == "__main__":
    unittest.main()
