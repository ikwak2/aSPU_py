#!/usr/bin/env python

def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def rankdata(a, method='average'):
    n = len(a)
    ivec=rank_simple(a)
    svec=[a[rank] for rank in ivec]
    sumranks = 0
    dupcount = 0
    newarray = [0]*n
    for i in xrange(n):
        sumranks += i
        dupcount += 1
        if i==n-1 or svec[i] != svec[i+1]:
            for j in xrange(i-dupcount+1,i+1):
                if method=='average':
                    averank = sumranks / float(dupcount) + 1
                    newarray[ivec[j]] = averank
                elif method=='max':
                    newarray[ivec[j]] = i+1
                elif method=='min':
                    newarray[ivec[j]] = i+1 -dupcount+1
                else:
                    raise NameError('Unsupported method')
            
            sumranks = 0
            dupcount = 0
            
            
    return newarray
