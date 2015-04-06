#!/usr/bin/python
import pdb

def addVertex(G, node, visited, edges):
    visited.add(node)
    for x in G[node]:
        if x[0] not in visited:
            edges.append((x[0], x[1]))

def addCheapest(G, visited, edges):
    minCost = float('inf')
    minKey = None
    for x in edges:
        if x[0] not in visited and x[1] < minCost:
            minKey = x[0]
            minCost = x[1]
    addVertex(G, minKey, visited, edges)
    return minCost

def mstWeight(G):
    visited = set()
    edges = []
    addVertex(G, 1, visited, edges)
    cost = 0
    while len(visited) < len(G):
        cost += addCheapest(G, visited, edges)
    return cost
