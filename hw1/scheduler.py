#!/usr/bin/python
# Input array of [weight, length] pairs
def calcCost(jobs):
    sum = 0
    endingTime = 0
    for job in jobs:
        endingTime += job[1]
        sum += endingTime * job[0]
    return sum

def weightedSumDifference(weights, lengths):
    jobs = zip(weights, lengths)
    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    jobs = sorted(jobs, key=lambda x: x[0]-x[1], reverse=True)
    return calcCost(jobs)

def weightedSumRatio(weights, lengths):
    jobs = zip(weights, lengths)
    jobs = sorted(jobs, key=lambda x: float(x[0])/float(x[1]), reverse=True)
    return calcCost(jobs)
