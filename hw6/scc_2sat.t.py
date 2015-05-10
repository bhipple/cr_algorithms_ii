#!/usr/bin/python
import unittest
from scc_2sat import *

def loadFile(filePath):
    fh = open(filePath)
    G = {}
    Grev = {}
    boolCt = int(fh.readline())
    for i in range(-1*boolCt, boolCt+1):
        G[i] = []
        Grev[i] = []

    for parts in map(lambda x:x.split(), fh.readlines()):
        x = int(parts[0])
        y = int(parts[1])
        G[-1 * x].append(y)
        G[-1 * y].append(x)
        Grev[x].append(-1*y)
        Grev[y].append(-1*x)

    return [G, Grev]

class TestUnit(unittest.TestCase):
    def setUp(self):
        pass

    def test_load(self):
        [G, Grev] = loadFile('instances/2sat1.txt')
        self.assertEqual(200001, len(G));
        self.assertEqual(200001, len(Grev));

    def test_satisfiable(self):
        [G, Grev] = loadFile('instances/satisfiable.txt')
        self.assertTrue(satisfiable(G, Grev))

    def test_unsatisfiable(self):
        [G, Grev] = loadFile('instances/unsatisfiable.txt')
        self.assertFalse(satisfiable(G, Grev))

    def test_hw_1(self):
        G,Grev = loadFile('instances/2sat1.txt')
        print "Instance 1 is: %s" % satisfiable(G, Grev)

    def test_hw_2(self):
        G,Grev = loadFile('instances/2sat2.txt')
        print "Instance 2 is: %s" % satisfiable(G, Grev)

    def test_hw_3(self):
        G,Grev = loadFile('instances/2sat3.txt')
        print "Instance 3 is: %s" % satisfiable(G, Grev)

    def test_hw_4(self):
        G,Grev = loadFile('instances/2sat4.txt')
        print "Instance 4 is: %s" % satisfiable(G, Grev)

    def test_hw_5(self):
        G,Grev = loadFile('instances/2sat5.txt')
        print "Instance 5 is: %s" % satisfiable(G, Grev)

    def test_hw_6(self):
        G,Grev = loadFile('instances/2sat6.txt')
        print "Instance 6 is: %s" % satisfiable(G, Grev)

if __name__ == '__main__':
    unittest.main()
