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
    for i in range(1, len(G) + 1):
        for v in G:
            minCost = A[i-1][v] or float('inf')
            for inc in G[v].ins:
                minCost = min(minCost, A[i-1][inc[0]] + inc[1])
            A[i][v] = minCost
    return A

def checkCycle(A):
    return A[len(A)-1] != A[len(A)-2]

def bellmanFord(G, s):
    A = bellmanInit(G, s)
    A = bellmanBody(G, A)
    if checkCycle(A):
        return False

    return A[len(A)-1]

def shortestShortestPath(nodeToDists):
    minPath = float('inf')
    for node in nodeToDists:
        minPath = min(minPath, min(node.values()))
    return minPath

def getStarters(G):
    starters = []
    for key in G:
        outs = map(lambda x: x[1], G[key].outs)
        if(min(outs + [1]) <= 0):
            starters.append(key)
    return starters

def allPairsShortestPaths(G):
    nodeNumToDistAllOthers = []

    starters = getStarters(G)
    print "Starters = %s" % starters
    ct = 0
    for s in starters:
        ct += 1
        print "%s (%s of %s)" % (s, ct, len(starters))
        thisNodesDists = bellmanFord(G, s)
        if not thisNodesDists:
            return False
        nodeNumToDistAllOthers.append(thisNodesDists)

    return shortestShortestPath(nodeNumToDistAllOthers)
