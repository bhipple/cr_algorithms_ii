#!/usr/bin/python

class Node():
    def __init__(self):
        self.leader = self
        self.clusterSize = 1
        self.followers = [self]

def union(l1, l2):
    if l2.clusterSize > l1.clusterSize: return union(l2, l1)

    l1.clusterSize += l2.clusterSize
    for node in l2.followers:
        node.leader = l1
        l1.followers.append(node)

def max_spacing_k_clustering(k, nodes, edges):
    numClusters = len(nodes) - 1
    for i in range(len(edges)):
        v1 = nodes[edges[i][1]]
        v2 = nodes[edges[i][2]]

        l1 = v1.leader
        l2 = v2.leader

        if l1 == l2:
            continue

        if numClusters == k:
            break

        union(l1, l2)
        numClusters -= 1

    return edges[i][0]
