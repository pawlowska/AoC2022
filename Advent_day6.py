# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:22:37 2022

@author: Monik
"""

# %% load data

f_test='day6_test.txt'
f_in='day6_input.txt'

with open(f_in) as f:
    lines=f.readlines()

# %% solve
ile=4 #number of distincts character to search

for l in lines:
    i=ile-1
    len1, len2=ile+1, ile+1 #init for the while loop
    while(len1*len2!=ile**2):
        i+=1
        substring=l[i-ile: i]
        len1=len(list(substring))
        len2=len(set(list(substring))) #set contains unique elements
    print(i)