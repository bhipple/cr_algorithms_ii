#!/usr/bin/python

class Node():
    def __init__(self):
        self.adj = []

def initDPArray(nodes):
    dist = []
    n = len(nodes) + 1
    for k in range(n):
        dist.append([[]]*n)

    return dist

def runLoops(nodes, dist):
    return 0

def checkCycle(dist):
    return False

def floyd_warshall(nodes):
    dist = initDPArray(nodes)
    return 0
