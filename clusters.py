#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:54:45 2019

@author: Frej
"""
import numpy as np


def clusters(A):
    clusters = 0
    for row in range(np.size(A, 0)):
        for col in range(np.size(A, 1)):
            if A[row][col]:
                clusters += 1
                removeNeighbors(row, col, A)
    return clusters


def removeNeighbors(row, col, A):
    A[row][col] = False
    for r, c in neighbors(row, col, A):
        if A[r][c]:
            removeNeighbors(r, c, A)


def neighbors(row, col, A):
    rows = np.size(A, 0)
    cols = np.size(A, 1)
    return [(row, (col+1) % cols), (row, (col-1) % cols), ((row+1) % rows, col), ((row-1) % rows, col)]


print(clusters([[True, False], [False, True]]))
