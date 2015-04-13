#!/usr/bin/python
import unittest
from clustering import *

# Input file has the following format:
# Line 1 gives the number of nodes in the Graph
# Each other line is in the format:
#   [edge i node a][edge i node b][edge i cost]
# Distances are positive but not necessarily distinct
def loadFile(filename):
    edges = []
    nodes = [Node()] # Packing in garbage in index 0, to avoid off-by-one confusion
    with open(filename, 'r') as fh:
        n = int(fh.readline())
        map(lambda x: nodes.append(Node()), [x for x in range(1,n+1)])

        for parts in map(lambda x: x.split(), fh.readlines()):
            v1 = int(parts[0])
            v2 = int(parts[1])
            cost = int(parts[2])
            edges.append((cost, v1, v2))

    edges = sorted(edges, cmp=lambda x,y: cmp(x[0], y[0]))
    return nodes, edges

class Component_Tester(unittest.TestCase):
    def test_node(self):
        a = Node()
        self.assertEqual(a, a.leader)
        self.assertEqual(1, a.clusterSize)

        b = Node()
        self.assertNotEqual(a.leader, b.leader)
        a.leader = b.leader
        self.assertEqual(a.leader, b.leader)

    def test_union(self):
        a = Node()
        b = Node()
        c = Node()
        union(a,b)
        self.assertEqual(a.leader, b.leader)
        self.assertEqual(2, a.leader.clusterSize)

        union(b.leader,c.leader)
        self.assertEqual(3, b.leader.clusterSize)
        self.assertEqual(b.leader, c.leader)
        self.assertEqual(a.leader, c.leader)
        self.assertEqual(a.leader.clusterSize, c.leader.clusterSize)


class HW1_Tester(unittest.TestCase):
    def test_loading_file(self):
        [nodes, edges] = loadFile('line.txt')
        self.assertEqual(9, len(nodes))
        last = edges[0]
        for edge in edges[1:]:
            self.assertGreaterEqual(edge[0], last[0])
            last = edge

        [nodes, edges] = loadFile('grid.txt')
        self.assertEqual(10, len(nodes))
        last = edges[0]
        for edge in edges[1:]:
            self.assertGreaterEqual(edge[0], last[0])
            last = edge

        [nodes, edges] = loadFile('simple.txt')
        self.assertEqual(6, len(nodes))

    def test_simple(self):
        [nodes, edges] = loadFile('simple.txt')
        self.assertEqual(5, max_spacing_k_clustering(2, nodes, edges))

        [nodes, edges] = loadFile('simple.txt')
        self.assertEqual(4, max_spacing_k_clustering(3, nodes, edges))

        [nodes, edges] = loadFile('simple.txt')
        self.assertEqual(3, max_spacing_k_clustering(4, nodes, edges))

    def test_line(self):
        [nodes, edges] = loadFile('line.txt')
        self.assertEqual(6, max_spacing_k_clustering(2, nodes, edges))

        [nodes, edges] = loadFile('line.txt')
        self.assertEqual(5, max_spacing_k_clustering(3, nodes, edges))

        [nodes, edges] = loadFile('line.txt')
        self.assertEqual(2, max_spacing_k_clustering(4, nodes, edges))

    def test_grid(self):
        [nodes, edges] = loadFile('grid.txt')
        self.assertEqual(4472, max_spacing_k_clustering(2, nodes, edges))

        [nodes, edges] = loadFile('grid.txt')
        self.assertEqual(3606, max_spacing_k_clustering(3, nodes, edges))

        [nodes, edges] = loadFile('grid.txt')
        self.assertEqual(1414, max_spacing_k_clustering(4, nodes, edges))

    def test_hw1(self):
        [nodes, edges] = loadFile('clustering1.txt')
        print "\nHW1 Answer is: %s\n" % max_spacing_k_clustering(4, nodes, edges)

if __name__ == "__main__":
    unittest.main()
