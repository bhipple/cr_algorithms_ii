#!/usr/bin/python
import pdb
from priorityDictionary import *

class Node():
    def __init__(self):
        self.outs = []
        self.ins = []
        self.weight = 0

def bellmanInit(G, s):
    A = {}
    for i in range(len(G) + 1):
        A[i] = {}
        for key in G:
            A[i][key] = float('inf')

    A[0][s] = 0
    return A

def bellmanBody(G, A):
    candidates = G.keys()
    for i in range(1, len(G) + 1):
        somethingChanged = False
        for v in candidates:
            minCost = A[i-1][v] or float('inf')
            for inc in G[v].ins:
                minCost = min(minCost, A[i-1][inc[0]] + inc[1])

            A[i][v] = minCost
            if A[i][v] != A[i-1][v]:
                somethingChanged = True

        if not somethingChanged:
            break
    return A[i]

def checkCycle(Ai, Ai1):
    return Ai != Ai1

def bellmanFord(G, s):
    A = bellmanInit(G, s)
    A = bellmanBody(G, A)

    """
    if checkCycle(Ai, Ai1):
        return False
    """

    return A

def getStarters(G):
    starters = []
    for key in G:
        outs = map(lambda x: x[1], G[key].outs)
        ins = map(lambda x: x[1], G[key].ins)
        if ((min(ins + [1])) <= 0):
            continue
        if(min(outs + [1]) <= 0):
            starters.append(key)

    return starters

def allPairsShortestPaths(G):
    nodeNumToDistAllOthers = []

    starters = getStarters(G)
    print "\nStarters = %s" % starters
    ct = 0
    fact = float(100 / float(len(starters)))
    minSoFar = float('inf')
    for s in starters:
        ct += 1
        print "%s (%s perc) (min = %s)" % (s, float(ct) * fact, minSoFar)

        thisNodesDists = bellmanFord(G, s)
        if not thisNodesDists:
            pdb.set_trace()
            return False
        minSoFar = min(minSoFar, min(thisNodesDists.values()))

    return minSoFar
