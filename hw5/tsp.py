#!/usr/bin/python
import itertools
import math
import time

import pdb

def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def StoKey(S):
    key = int(0)
    for val in S:
        key = key | (1 << val)
    return key

def tsp(cities):
    # A is first indexed by S, and secondly indexed by
    # the destination vertex.  So A[S][j] = the length
    # of the shortest path from start to j, using every
    # vertex in S exactly once.
    A = [[float('inf')] * len(cities) for x in xrange(2**len(cities))]
    indexes = tuple([i for i in range(0,len(cities))])

    # As a base case, A[S][0] = 0 if S == {0} and
    # infinity otherwise
    A[1][0] = 0

    # For each subproblem size + the start city (0)
    for m in range(1, len(cities)):
        # For each combination of the non-start vertices
        # of that subproblem size
        print "m = %s at time %s" % (m, time.strftime("%H:%M:%S"))
        for comb in itertools.combinations(indexes[1:], m):
            S = tuple([0] + [i for i in comb])
            combKey = StoKey(S)

            # For each j in S, calculate the shortest path
            # from 0 to j that visits every node in S once
            for j in S[1:]:
                # A shortest path from 0 to j using nodes in S
                # is the shortest path from 0 to any k in S, k!=j,
                # plus the distance from k to j
                subKey = StoKey([i for i in S if i != j])
                cost = float('inf')
                for k in S:
                    if k == j: continue # replace this line with list comprehension above?
                    cost = min(cost, A[subKey][k] + dist(cities[j], cities[k]))
                A[combKey][j] = cost

    # Now, find the j that is the shortest ending point.
    cost = float('inf')
    graphKey = StoKey(indexes)
    for j in range(1, len(cities)):
        cost = min(cost, A[graphKey][j] + dist(cities[j], cities[0]))
    return cost
