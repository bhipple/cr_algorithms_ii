#!/usr/bin/python
import unittest
from floyd_warshall import *

# Input file has the following format:
# Line 1 gives the number of nodes in the Graph
# Each other line is in the format:
#   [edge i node a][edge i node b][edge i cost]
def loadFile(filename):
    nodes = []
    with open(filename, 'r') as fh:
        n = int(fh.readline().split()[0])
        # Packing in garbage in index 0, to avoid off-by-one confusion
        map(lambda x: nodes.append(Node()), [x for x in range(0,n+1)])

        for parts in map(lambda x: x.split(), fh.readlines()):
            v1 = int(parts[0])
            v2 = int(parts[1])
            cost = int(parts[2])
            nodes[v1].outs.append([v2, cost])
            nodes[v2].ins.append([v1, cost])
    return nodes

class Component_Tester(unittest.TestCase):
    def test_all_files_get_correct_node_count(self):
        nodes = loadFile('g1.txt')
        self.assertEqual(1001, len(nodes))
        for node in nodes[1:]:
            self.assertTrue(len(node.outs))

        nodes = loadFile('g2.txt')
        self.assertEqual(1001, len(nodes))

        nodes = loadFile('g3.txt')
        self.assertEqual(1001, len(nodes))

    def test_A_initialization(self):
        nodes = loadFile('g1.txt')
        A = bellmanInit(nodes, 1)
        n = len(nodes)
        self.assertEqual(n, len(A))
        self.assertEqual(n, len(A[0]))

    def test_johnson_init(self):
        nodes = loadFile('6.txt')
        johnsonReweighting(nodes)
        for node in nodes:
            for out in node.outs:
                self.assertGreaterEqual(out[1], 0)

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

class HW_Runner():
    def test_first_graph(self):
        nodes = loadFile('g1.txt')
        print "\nFor file g1, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)

    def test_second_graph(self):
        nodes = loadFile('g2.txt')
        print "\nFor file g2, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)

    def test_third_graph(self):
        nodes = loadFile('g3.txt')
        print "\nFor file g3, the shortest shortest path is:"
        print allPairsShortestPaths(nodes)

if __name__ == "__main__":
    unittest.main()
