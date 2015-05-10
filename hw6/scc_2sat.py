#!/usr/bin/python
import sys
sys.setrecursionlimit(1000000)

visited = {}
leader = {}
finishOrder = []
s = 0

def leaderToSCCs(leader):
    sccs = {}
    for scc in leader.values():
        sccs[scc] = []
    map(lambda x: sccs[leader[x]].append(x), leader.keys())
    return sccs

def dfs(G, i):
    global visited, leader, s, finishOrder
    visited[i] = True
    leader[i] = s

    for j in G[i]:
        if not j in visited:
            dfs(G, j)

    finishOrder.append(i)

def dfsLoop(G, seq):
    global visited, s, finishOrder
    visited.clear()
    s = 0

    for i in seq:
        if not i in visited:
            s = i
            dfs(G, i)

def scc(G, Grev):
    global finishOrder, leader
    finishOrder = []
    leader = {}

    #vals = len(G) / 2
    dfsLoop(Grev, Grev.keys())
    finishOrder.reverse()
    dfsLoop(G, finishOrder)

    return leaderToSCCs(leader)

def satisfiable(G, Grev):
    sccs = scc(G, Grev)
    for name in sccs:
        A = set()
        for node in sccs[name]:
            if -1*node in A: return False
            A.add(node)
    return True
