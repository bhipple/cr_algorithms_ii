#!/usr/bin/python
import unittest
from tsp import *

def loadFile(filename):
    cities = []
    with open(filename, 'r') as fh:
        header = fh.readline()
        cities = map(lambda x: (float(x.split()[0]), float(x.split()[1])), fh.readlines())
    return cities

class Component_Tester(unittest.TestCase):
    def test_loader(self):
        cities = loadFile('tsp.txt')
        self.assertEqual(25, len(cities))
        for city in cities:
            self.assertEqual(2, len(city))

    def test_powerset(self):
        combinations = [i for i in itertools.combinations([0,1,2,3,4], 2)]
        self.assertEqual(10, len(combinations))

    def test_dist(self):
        self.assertEqual(5, dist([0,0], [3,4]))


class Unit_Tester(unittest.TestCase):
    def test_line(self):
        cities = loadFile('line.txt')
        self.assertEqual(12, tsp(cities))

    def test_rectangle(self):
        cities = loadFile('rectangle.txt')
        #self.assertEqual(10, tsp(cities))

class HW_Runner(unittest.TestCase):
    def test_hw(self):
        pass
        #cities = loadFile('tsp.txt')
        #self.assertEqual(0, tsp(cities))

if __name__ == "__main__":
    unittest.main()
