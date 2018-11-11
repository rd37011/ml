#!/usr/bin/env python

import csv
import random
import numpy as np
import math

"""kmeans.py: K-Means clustering algorithm."""

__author__ = "Ryan Diaz"
__copyright_ = "Copyright 2018, University of Miami, Coral Gables, FL "


class _kmeans_:
    def __init__(self, p, label):
        self.point = p
        self.label = label


def init(data, k):
    centroids = []
    labeleddata = []
    length = len(data)

    for i in range(k):
        index = random.randint(0, length-1)
        centroids.append(data[index])  # assigns random centroids

    for d in data:
        d = np.array(d)
        p = _kmeans_(d, None)
        labeleddata.append(p) # list of _kmeans_ objects with points and blank labels

    return adjustpoints(centroids, labeleddata)


def adjustpoints(centroids, labeleddata):
    mndist = math.inf
    for d in labeleddata:
        for c in centroids:
            dist = np.sqrt(sum((d.point - c) ** 2))  # gets euclidean distance between point d and centroid c

            if dist < mndist:
                mndist = dist
                label = c

        mndist = math.inf
        d.label = label
    labeleddata = np.asarray(labeleddata)
    return centroids, labeleddata


def adjustcentroids(centroids, labeleddata):
    newcentroids = []
    sum = np.zeros(len(labeleddata[0].point))
    count = 0

    for c in centroids:
        c = np.array(c)
        sum = np.array(sum)

        for i in range(len(labeleddata)):

            if all(labeleddata[i].label == c):  # checking if label equal elementwise to c
                count += 1
                sum = sum + labeleddata[i].point

        sum = np.array(sum / count)
        newcentroids.append(sum)
        sum, count = 0, 0
    newcentroids = np.asarray(newcentroids)
    return newcentroids, labeleddata


def shouldstop(oldcentroids, centroids, iterations, maxiter):
    if np.array_equal(oldcentroids, centroids):
        return True
    if iterations < maxiter:
        return False
    return False


def kmeans():  # driver program
    k = 4
    maxiter = 30
    norm_data = loaddata()
    data = init(norm_data, k) # sets random centroids, None for labels in object array
    centroids, labeleddata = data

    iterations = 0
    oldcentroids = None

    while not shouldstop(oldcentroids, centroids, iterations, maxiter):  # while under max iter or centroids dont change
        oldcentroids = centroids
        iterations += 1
        centroids, labeleddata = adjustcentroids(centroids, labeleddata)
        centroids, labeleddata = adjustpoints(centroids, labeleddata)
        export(centroids, labeleddata)
        print(iterations)
        for c in centroids:
            print(c)



def export(centroids, labeleddata):
    csv.register_dialect('output', delimiter=' ', lineterminator="\n")
    with open('kmeans_2ddata.csv', 'a', newline="\n") as f:
        writer = csv.writer(f)
        for c in centroids:
            writer.writerow(c)
            writer.writerow("\n")
            for p in labeleddata:
                if all(p.label == c):
                    writer.writerow(p.label)
                    writer.writerow(p.point)
            writer.writerow("\n")
    return 0



def loaddata():
    dataset = []
    with open('2dtrain_data.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            row = list(map(float, row))
            """
            mn = min(row)
            mx = max(row)
            for i in range(len(row)):
                if mx - mn == 0:
                    row[i] = 0.0
                else:
                    row[i] = (row[i] - mn)/(mx - mn)
            """
            dataset.append(row)
        return dataset


kmeans()

