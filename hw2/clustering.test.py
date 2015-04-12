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
def fileToGraph1(filename):
    return {}

# For question 2, we have a much larger graph, with each row in the format:
#   [# of nodes] [# of bits for each node's label]
#   [first bit of node 1] ... [last bit of node 1]
#   [first bit of node 2] ... [last bit of node 2]
# Distances between the nodes are the Hamming distance between the two nodes' labels
def fileToGraph2(filename):
    return {}


class HW1_Tester(unittest.TestCase):
    def test_loading_file(self):
        G = fileToGraph1('line.txt')
        self.assertEqual(8, len(G))

        G = fileToGraph1('grid.txt')
        self.assertEqual(9, len(G))

        G = fileToGraph1('simple.txt')
        self.assertEqual(5, len(G))

    def test_line(self):
        G = fileToGraph1('line.txt')

        # Total distance as a function of k and G
        self.assertEqual(6, max_spacing_k_clustering(2, G))
        self.assertEqual(5, max_spacing_k_clustering(3, G))
        self.assertEqual(2, max_spacing_k_clustering(4, G))

    def test_grid(self):
        G = fileToGraph1('grid.txt')

        # Total distance as a function of k and G
        self.assertEqual(4472, max_spacing_k_clustering(2, G))
        self.assertEqual(3606, max_spacing_k_clustering(3, G))
        self.assertEqual(1414, max_spacing_k_clustering(4, G))


    def hw1(self):
        G = fileToGraph1('clustering1.txt')
        print max_spacing_k_clustering(4, G)

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
        G = fileToGraph2('clustering_big.txt')
        self.assertEqual(200000, len(G))

    def hw2(self):
        G = fileToGraph1('clustering_big.txt')
        print max_spacing_k_clustering(4, G)


if __name__ == "__main__":
    unittest.main()
