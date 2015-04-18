#!/usr/bin/python

def calcDecision(A, items, i, x):
    skipIt = 0
    useIt = 0

    if i > 0:
        skipIt = A[i-1][x]

    remainder = x - items[i][1]
    if remainder >= 0:
        useIt = A[i-1][remainder] + items[i][0]

    return max(skipIt, useIt)


def knapsack(size, items):
    n = len(items)
    A = []
    for i in range(n):
        A.append([0]*(size+1))

    for i in range(n):
        for x in range(size+1):
            A[i][x] = calcDecision(A, items, i, x)

    return A[n-1][size]
