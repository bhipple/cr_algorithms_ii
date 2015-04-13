#!/usr/bin/python
import unittest
from clustering import *

def hamming_distance(a, b):
    return 0

# Input file has the following format:
# Line 1 gives the number of nodes in the Graph
# Each other line is in the format:
#   [edge i node a][edge i node b][edge i cost]
# Distances are positive but not necessarily distinct
def loadFile(filename):
    edges = []
    nodes = [None] # Packing in garbage in index 0, to avoid off-by-one confusion
    return nodes, edges

# For question 2, we have a much larger graph, with each row in the format:
#   [# of nodes] [# of bits for each node's label]
#   [first bit of node 1] ... [last bit of node 1]
#   [first bit of node 2] ... [last bit of node 2]
# Distances between the nodes are the Hamming distance between the two nodes' labels
def loadFile2(filename):
    return {}


class HW1_Tester(unittest.TestCase):
    def test_loading_file(self):
        [nodes, edges] = loadFile('line.txt')
        self.assertEqual(9, len(nodes))

        [nodes, edges] = loadFile('grid.txt')
        self.assertEqual(10, len(nodes))

        [nodes, edges] = loadFile('simple.txt')
        self.assertEqual(6, len(nodes))

    def d_test_line(self):
        [nodes, edges] = loadFile('line.txt')

        # Total distance as a function of k and nodes
        self.assertEqual(6, max_spacing_k_clustering(2, nodes, edges))
        self.assertEqual(5, max_spacing_k_clustering(3, nodes, edges))
        self.assertEqual(2, max_spacing_k_clustering(4, nodes, edges))

    def d_test_grid(self):
        [nodes, edges] = loadFile('grid.txt')

        # Total distance as a function of k and nodes
        self.assertEqual(4472, max_spacing_k_clustering(2, nodes, edges))
        self.assertEqual(3606, max_spacing_k_clustering(3, nodes, edges))
        self.assertEqual(1414, max_spacing_k_clustering(4, nodes, edges))


    def hw1(self):
        [nodes, edges] = loadFile('clustering1.txt')
        print max_spacing_k_clustering(4, nodes, edges)

class HW2_Tester(unittest.TestCase):
    def disabled_test_hamming(self):
        self.assertEqual(3, hamming_distance("Benn", "Inna"))

        a = "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
        b = "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
        self.assertEqual(3, hamming_distance(a, b))

        a = "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
        b = "1 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
        self.assertEqual(4, hamming_distance(a, b))

    def disabled_test_loading_file2(self):
        [nodes, edges] = loadFile2('clustering_big.txt')
        self.assertEqual(200000, len(nodes))

    def hw2(self):
        [nodes, edges] = loadFile('clustering_big.txt')
        print max_spacing_k_clustering(4, nodes, edges)


if __name__ == "__main__":
    unittest.main()
