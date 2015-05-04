#!/usr/bin/python
import unittest
from tsp import *

def loadFile(filename):
    cities = []
    with open(filename, 'r') as fh:
        header = fh.readline()
        cities = map(lambda x: (float(x.split()[0]), float(x.split()[1])), fh.readlines())
    return cities

class TestComponents(unittest.TestCase):
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

    def test_key_hash(self):
        self.assertEqual(17, StoKey((0,4)))
        self.assertEqual(145, StoKey((0,4,7)))
        self.assertEqual(16777361, StoKey((0,4,7,24)))

class TestSample(unittest.TestCase):
    def test_line(self):
        cities = loadFile('line.txt')
        self.assertEqual(12, tsp(cities))

    def test_rectangle(self):
        cities = loadFile('rectangle.txt')
        self.assertEqual(10, tsp(cities))

    def test_magic(self):
        cities = loadFile('18_cities.txt')
        self.assertAlmostEqual(3.501, tsp(cities), places=3)


class TestHW(unittest.TestCase):
    def test_hw(self):
        print "\nStarting HW question:"
        cities = loadFile('tsp.txt')
        print "\n\nThe answer to the HW question is: %s\n" % tsp(cities)

if __name__ == "__main__":
    unittest.main()
