#!/usr/bin/python
# -*- Coding: utf-8 -*-



import numpy as np

from scipy.spatial.distance import euclidean


import csv

a = [list(map(float,line.rstrip().split(","))) for line in open('k_sample1.csv').readlines()]

 
b = [list(map(float,line.rstrip().split(","))) for line in open('k_client1.csv').readlines()]


print(1 / (1 + (euclidean(a, b))))