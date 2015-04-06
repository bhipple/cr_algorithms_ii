#!/usr/bin/python
import unittest
from prim import *

def parseFile(fileName):
    G = {}
    with open(fileName, 'r') as f:
        f.readline() #kill header
        for line in f:
            parts = line.split()
            v1 = int(parts[0])
            v2 = int(parts[1])
            cost = int(parts[2])

            if v1 in G:
                G[v1].append((v2, cost))
            else:
                G[v1] = [(v2, cost)]

            if v2 in G:
                G[v2].append((v1, cost))
            else:
                G[v2] = [(v1, cost)]
        return G

class PrimTest(unittest.TestCase):
    def test_count(self):
        G = parseFile('edges.txt')
        self.assertEqual(500, len(G.keys()))

    def test_unit1(self):
        G = parseFile('prim_7.txt')
        self.assertEqual(7, mstWeight(G))

    def test_unit2(self):
        G = parseFile('prim_37.txt')
        self.assertEqual(37, mstWeight(G))

    def test_homework(self):
        G = parseFile('edges.txt')
        print "\nMST Weight: %s\n" % mstWeight(G)

if __name__ == '__main__':
    unittest.main()
