#!/usr/bin/python
import unittest
from scheduler import *

def parseFile(fileName):
    with open(fileName, 'r') as f:
        weights = []
        lengths = []
        f.readline() # consume the number-of-jobs line
        for line in f:
            parts = line.split()
            weights.append(int(parts[0]))
            lengths.append(int(parts[1]))
        return weights, lengths

class NaiveGreedy(unittest.TestCase):
    def test_diff_simple(self):
        self.assertEqual(1, weightedSumDifference([1], [1]))

    def test_diff_two_jobs(self):
        self.assertEqual(4, weightedSumDifference([1,2], [1,1]))

    def test_diff_three_where_sort_ties_matter(self):
        self.assertEqual(192, weightedSumDifference([1,5,10], [2,5,10]))

    def test_diff_file_from_forums(self):
        weights, lengths = parseFile('61545-60213.txt')
        self.assertEqual(10, len(weights))
        self.assertEqual(10, len(lengths))
        self.assertEqual(61545, weightedSumDifference(weights, lengths))

    def test_ratio_file_from_forums(self):
        weights, lengths = parseFile('61545-60213.txt')
        self.assertEqual(60213, weightedSumRatio(weights, lengths))

    def test_real_difference(self):
        weights, lengths = parseFile('jobs.txt')
        print "\nAnswer to Question 1:", weightedSumDifference(weights, lengths), "\n"

    def test_real_ratio(self):
        weights, lengths = parseFile('jobs.txt')
        print "\nAnswer to Question 2:", weightedSumRatio(weights, lengths), "\n"

if __name__ == '__main__':
    unittest.main()
