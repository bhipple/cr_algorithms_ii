#!/usr/bin/python

import unittest
from knapsack import *

def loadFromFile(filename):
    with open(filename, 'r') as fh:
        header = fh.readline().split()
        size = int(header[0])
        lines = map(lambda x: x.split(), fh.readlines())
    items = map(lambda x: (int(x[0]), int(x[1])), lines)
    return size, items

class TestLoader(unittest.TestCase):
    def test_load(self):
        size, items = loadFromFile('knapsack1.txt')
        self.assertEqual(10000, size)
        self.assertEqual(100, len(items))

class Problem1(unittest.TestCase):
    def test_class_example(self):
        size, items = loadFromFile('class_example.txt')
        self.assertEqual(8, knapsack(size, items))

    def test_hw1(self):
        size, items = loadFromFile('knapsack1.txt')
        print "\nHW1 Answer: %s\n" % knapsack(size, items)

class Problem2(unittest.TestCase):
    def d_test_hw2(self):
        size, items = loadFromFile('knapsack_big.txt')
        print "\nHW2 Answer: %s\n" % knapsack(size, items)


if __name__ == "__main__":
    unittest.main()
