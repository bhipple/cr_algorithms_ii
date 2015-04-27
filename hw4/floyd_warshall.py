#!/usr/bin/python
import pdb

class Node():
    def __init__(self):
        self.outs = []
        self.ins = []
        self.weight = 0

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
        return False

    return A[len(A)-1]

def johnsonReweighting(nodes):
    # Preprocess with new start node 0
    for i in range(1, len(nodes)):
        nodes[i].ins.append([0, 0])
        nodes[0].outs.append([i,0])

    # Find vertex weights, or a negative cycle
    dists = bellmanFord(nodes, 0)
    if not dists:
        return False # Negative cycle

    # Reweight the edges
    for i in range(1, len(nodes)):
        thisNode = nodes[i]
        thisNode.weight = dists[i]

        for out in thisNode.outs:
            out[1] = out[1] + dists[i] - dists[out[0]]

    return True

def addCheapestNode(nodes, visited, A):
    candidate = None
    minSoFar = float('inf')
    for vertex in visited:
        for edgepair in nodes[vertex].outs:
            if edgepair[0] not in visited:
                if A[vertex]+edgepair[1] < minSoFar:
                    minSoFar = A[vertex]+edgepair[1]
                    candidate = edgepair[0]
    if candidate is None:
        # No more nodes reachable from current set
        return False

    visited.append(candidate)
    A[candidate] = minSoFar
    return True

def dijkstra(nodes,s):
    visited = []
    A = [float('inf')] * len(nodes)
    visited.append(s)
    A[s]=0
    while addCheapestNode(nodes, visited, A):
        pass

    # Post-process to remove weights
    for i in range(1,len(nodes)):
        A[i] = A[i] - nodes[s].weight + nodes[i].weight
    return A

def allPairsShortestPaths(nodes):
    if not johnsonReweighting(nodes):
        print "\nNegative cycle detected."
        return False

    nodeNumToDistAllOthers = []
    nodeNumToDistAllOthers.append([float('inf')]) # Off by one filler
    for s in range(1, len(nodes)):
        print s
        nodeNumToDistAllOthers.append(dijkstra(nodes, s))

    print nodeNumToDistAllOthers
    return min([min(x) for x in nodeNumToDistAllOthers])
