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

def allPairsShortestPaths(G):
    nodeNumToDistAllOthers = []
    for s in G:
        print s
        thisNodesDists = bellmanFord(G, s)
        if not thisNodesDists:
            return False
        nodeNumToDistAllOthers.append(thisNodesDists)

    return shortestShortestPath(nodeNumToDistAllOthers)
