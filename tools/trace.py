from IPython import embed
from matplotlib.pyplot import *
from numpy import random
from numpy.random import rand
import csv


def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L

nameList = []
list = []

''' position '''
path1 = '../_build/cpp/results.csv'

with open(path1,'r') as dataFile1:
    reader = csv.reader(dataFile1)
    i = 0
    for row in reader:
        if i == 2:
            for k in range(n+1):
                list[k].append(float(row[k]))
        if i == 1:
            i = 2;
            N = float(row[0])
            n = int(row[1])
            for k in range(n+1):
                list.append([])
        if i == 0:
            i = 1
            for k in row:
                nameList.append(k)


embed()

'''for k in range(n):
    figure()
    plot(list[0],list[k+1])
    title(nameList[k+1])
    grid()

show()'''