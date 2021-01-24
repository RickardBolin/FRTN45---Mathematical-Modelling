#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:54:45 2019

@author: Frej
"""
import numpy as np

def clusters(A):
    l=len(A)
    
    def removeNeighbors(i):
        j=i
        while A[j]:
            A[j]=False
            j=(j+1)%l
        j=(i+1)%l
        while A[j]:
            A[j]=False
            j=(j+1)%l
    
    clusters=0
    for n in range(l):
            if A[n]:
                clusters+=1
                removeNeighbors(n)
    return clusters