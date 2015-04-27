#!/usr/bin/python
import pdb
from priorityDictionary import *

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

def dijkstra(G, start):
    D = {}  # Node -> distance
    P = {}  # Node -> predecessor in path
    Q = priorityDictionary()  # Node -> cost to add
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

def postProcess(D, thisWeight, weights):
    A = []
    for key in D:
        A.append(D[key] - weights[key] + thisWeight)
    return A

def convertToDictRep(nodes):
    G = {}
    weights = {}
    for i in range(1,len(nodes)):
        weights[i] = nodes[i].weight
        outs = {}
        for out in nodes[i].outs:
            outs[out[0]] = out[1]
        G[i] = outs

    return G, weights

def allPairsShortestPaths(nodes):
    if not johnsonReweighting(nodes):
        print "\nNegative cycle detected."
        return False

    G, weights = convertToDictRep(nodes)
    nodeNumToDistAllOthers = [[float('inf')]] # OBOE filler
    for s in range(1, len(nodes)):
        D = dijkstra(G, G[s])
        distances = postProcess(D, nodes[s].weight, weights)
        print s
        nodeNumToDistAllOthers.append(distances)

    print nodeNumToDistAllOthers
    return min([min(x) for x in nodeNumToDistAllOthers])
