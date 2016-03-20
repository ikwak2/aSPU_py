#!/usr/bin/env python 

import sys
import numpy as np
from numpy.linalg import eig
from util import rankdata

Zs = np.loadtxt(sys.argv[1])
corPhe = np.loadtxt(sys.argv[2])
corSNP = np.loadtxt(sys.argv[3])
nperm = int(sys.argv[4])
print nperm

pow1 = np.array([1,2,4,8])
pow2 = np.array([1,2,4,8])
#nperm = 10

#print Zs
#print corPhe
#print corSNP

nsnp = Zs.shape[0]
nphe = Zs.shape[1]
    
V = corSNP
U = corPhe

ev_U, evec_U = eig(U)
ev_U[ ev_U < 0] = 0
A = np.dot(np.dot(evec_U, np.diag(np.sqrt(ev_U))) , evec_U.T)
ev_V, evec_V = eig(V)
ev_V[ ev_V < 0] = 0
B = np.dot(np.dot(evec_V, np.diag(np.sqrt(ev_V))) , evec_V.T)

Ts = np.array([0 for i in range(len(pow1)*len(pow2))], dtype = "float64")
for p1 in range(len(pow1)) :
    for p2 in range(len(pow2)) :
        Zs2 = Zs**pow1[p1]
        Zs3 = Zs2.sum(axis = 0)**pow2[p2]
        Ts[p2 + p1*len(pow2)] = Zs3.sum()

        
pPerm0 = np.array( [0 for i in range(len(pow1)*len(pow2))], dtype = "float16")
T0s = np.array( [0 for i in range(nperm)], dtype = "float64")

for p1 in range(len(pow1)) :
    for p2 in range(len(pow2)) :
        np.random.seed(1)
        for b in range(nperm) :
            Zs0 = np.zeros( (nphe,nsnp) )
            for t in range(nphe) :
                Zs0[t,] = np.random.normal(0, 1, nsnp)
            Z0 = np.dot(np.dot(A,Zs0), B).T
            Z02 = Z0**pow1[p1]
            Z03 = Z02.sum(axis = 0)**pow2[p2]
            T0s[b] = Z03.sum()
        pPerm0[p2 + p1*len(pow2)] = sum(np.abs(T0s) >=  np.abs(Ts[p2 + p1*len(pow2)])) / float(nperm)
        rkT0s = np.array(rankdata(np.abs(T0s)))
        P0s = (nperm - rkT0s + 1) / nperm
        if p2 + p1*len(pow2) == 0 :
            minp0 = P0s.copy()
        else :
            minp0[ minp0 > P0s ] = P0s[ minp0 > P0s ]

Paspu =  (sum(minp0 <= pPerm0.min()) + 1) / float(nperm+1)

print "MTSPUsSets : " + str(pPerm0)
print "MTaSPUsSet : " + str(Paspu)



