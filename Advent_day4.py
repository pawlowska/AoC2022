# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:38:43 2022

@author: Monik
"""
# %%
def rangeStringToSet(r):
    a, b=map(int, r.split('-'))
    return set(range(a, b+1))

def parseRanges(l):
    rs=l.rstrip().split(',')
    sets=list(map(rangeStringToSet, rs))
    return(sets)    

def setsNeedAttention(s1, s2):
    return s1<=s2 or s2<=s1

# %% load data

f_test='day4_test.txt'
f_in='day4_input.txt'

with open(f_in) as f:
    lines=f.readlines()

allRanges=[parseRanges(l) for l in lines]

resBool=[setsNeedAttention(s1, s2) for s1, s2 in allRanges]

result1=sum(resBool)
# %% part2
resBool2=[not s1.isdisjoint(s2) for s1, s2 in allRanges]
result2=sum(resBool2)
