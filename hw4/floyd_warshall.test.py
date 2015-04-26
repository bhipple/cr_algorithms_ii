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
            nodes[v1].adj.append((v2, cost))

    return nodes

class Component_Tester(unittest.TestCase):
    def test_all_files_get_correct_node_count(self):
        nodes = loadFile('g1.txt')
        self.assertEqual(1001, len(nodes))
        for node in nodes[1:]:
            self.assertTrue(len(node.adj))

        nodes = loadFile('g2.txt')
        self.assertEqual(1001, len(nodes))

        nodes = loadFile('g3.txt')
        self.assertEqual(1001, len(nodes))

    def test_A_initialization(self):
        nodes = loadFile('g1.txt')
        A = initDPArray(nodes)
        n = len(nodes) + 1
        self.assertEqual(n, len(A))
        self.assertEqual(n, len(A[0]))
        self.assertEqual(n, len(A[0][0]))

#class HW1_Tester(unittest.TestCase):

if __name__ == "__main__":
    unittest.main()
