#!/usr/bin/python
import unittest
from floyd_warshall import *

# Input file has the following format:
# Line 1 gives the number of nodes in the Graph
# Each other line is in the format:
#   [edge i node a][edge i node b][edge i cost]
def loadFile(filename):
    G = {}
    with open(filename, 'r') as fh:
        n = int(fh.readline().split()[0])
        for i in range(1,n+1):
            G[i] = Node()

        for parts in map(lambda x: x.split(), fh.readlines()):
            v1 = int(parts[0])
            v2 = int(parts[1])
            cost = int(parts[2])
            G[v1].outs.append([v2, cost])
            G[v2].ins.append([v1, cost])
    return G

class Component_Tester(unittest.TestCase):
    def test_all_files_get_correct_node_count(self):
        G = loadFile('g1.txt')
        self.assertEqual(1000, len(G))
        for key in G:
            self.assertTrue(len(G[key].outs))

class Unit_Tester(unittest.TestCase):
    def test_neg_6(self):
        nodes = loadFile('6.txt')
        self.assertEqual(-6, allPairsShortestPaths(nodes))

    def test_neg_10k(self):
        nodes = loadFile('10003.txt')
        self.assertEqual(-10003, allPairsShortestPaths(nodes))

    def test_negative_cycle(self):
        nodes = loadFile('negative_cycle.txt')
        self.assertFalse(allPairsShortestPaths(nodes))

class HW_Runner(unittest.TestCase):
    """
    def test_first_graph(self):
        nodes = loadFile('g1.txt')
        print "\nFor file g1, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)

    def test_second_graph(self):
        nodes = loadFile('g2.txt')
        print "\nFor file g2, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)
    """

    def d_test_third_graph(self):
        nodes = loadFile('g3.txt')
        print "\nFor file g3, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)

if __name__ == "__main__":
    unittest.main()
