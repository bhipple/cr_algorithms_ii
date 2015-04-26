#!/usr/bin/python

class Node():
    def __init__(self):
        self.outs = []
        self.ins = []

def bellmanInit(nodes, s):
    A = []
    for i in range(len(nodes)):
        A.append([float('inf')] * len(nodes))

    A[0][s] = 0
    return A

def bellmanBody(nodes, A):
    for i in range(1, len(nodes)):
        for v in range(1, len(nodes)):
            minCost = A[i-1][v]
            for inc in nodes[v].ins:
                minCost = min(minCost, A[i-1][inc[0]] + inc[1])
            A[i][v] = minCost
    return A

def checkCycle(A):
    return A[len(A)-1] != A[len(A)-2]

def bellmanFord(nodes, s):
    A = bellmanInit(nodes, s)
    A = bellmanBody(nodes, A)
    if checkCycle(A):
        print "There is a negative cycle in the graph!"
        return False

    return A[len(A)-1]

def allPairsShortestPaths(nodes):
    nodeNumToDistAllOthers = []
    nodeNumToDistAllOthers.append([float('inf')]) # Off by one filler
    for s in range(1, len(nodes)):
        thisNodesDists = bellmanFord(nodes, s)
        if not thisNodesDists:
            return False
        nodeNumToDistAllOthers.append(thisNodesDists)


    return min([min(x) for x in nodeNumToDistAllOthers])
