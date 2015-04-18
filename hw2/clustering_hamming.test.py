#!/usr/bin/python
import unittest
from clustering import *

def hamming_distance(a, b):
    return sum(ch1 != ch2 for ch1, ch2 in zip(a,b))

# For question 2, we have a much larger graph, with each row in the format:
#   [# of nodes] [# of bits for each node's label]
#   [first bit of node 1] ... [last bit of node 1]
#   [first bit of node 2] ... [last bit of node 2]
# Distances between the nodes are the Hamming distance between the two nodes' labels
def loadFile2(filename):
    with open(filename, 'r') as fh:
        header = fh.readline()
        return map(lambda x: x.replace(' ', '').strip(), fh.readlines())

class HW2_Tester(unittest.TestCase):
    def test_hamming(self):
        self.assertEqual(3, hamming_distance("Benn", "Inna"))

        a = "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
        b = "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
        self.assertEqual(3, hamming_distance(a, b))

        a = "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
        b = "1 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
        self.assertEqual(4, hamming_distance(a, b))

    def test_loading_file2(self):
        nodes = loadFile2('clustering_big.txt')
        self.assertEqual(200000, len(nodes))
        for line in nodes:
            self.assertEqual(24, len(line))

        sorted(nodes)

    def test_smaller(self):
        nodes = loadFile2('clustering_smaller.txt')
        self.assertEqual(1000, len(nodes))

    def hw2(self):
        [nodes, edges] = loadFile('clustering_big.txt')
        print max_spacing_k_clustering(4, nodes, edges)

    def test_lol(self):
        nodes = loadFile2('clustering_big.txt')
        while True:
            for line in nodes:
                print '\033[92m' + line + line + line + '\033[0m'

if __name__ == "__main__":
    unittest.main()
