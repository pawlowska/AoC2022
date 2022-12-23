# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:40:25 2022

@author: Monik
"""

import numpy as np

# %% load data

f_test='day8_test.txt'
f_in='day8_input.txt'

with open(f_in) as f:
    lines=f.readlines()

trees=np.array([[int(s) for s in l.strip()] for l in lines])
r, c=trees.shape
    
# %% calculate visibility from outside for any tree, considering each direction separately first
temp=np.zeros((r, c))
temp[0,:]  =1
temp[-1,:] =1
temp[:,0]  =1
temp[:, -1]=1

left=np.copy(temp)
right=np.copy(temp)


for row in range(1, r-1):
    for col in range(1, c-1):
        if trees[row, col]>max(np.take(trees[row], range(0,col))):
            left[row, col]=1
        else:
            left[row, col]=0
        if trees[row][col]>max(np.take(trees[row], range(col+1, c))):
            right[row, col]=1
        else:
            right[row, col]=0

top=np.copy(temp)
bottom=np.copy(temp)

for col in range(1, c-1):
    for row in range(1, r-1):
        if trees[row, col]>max(np.take(trees[:,col], range(0, row))):
            top[row, col]=1
        else:
            top[row, col]=0
        if trees[row, col]>max(np.take(trees[:,col], range(row+1, r))):
            bottom[row, col]=1
        else:
            bottom[row, col]=0
            

visibility=left+right+top+bottom
print(np.count_nonzero(visibility>0)        )

# %%

def score(row, col):
    t=trees[row, col]
    #print('this tree has height', t)
    if(row==0 or row==r-1 or col==0 or col==c-1):
        #print('Edge!')
        return 0
    j=col-1
    l, rr, t, b=1, 1, 1, 1
    while(j>0 and trees[row,j]<trees[row, col]):
        l+=1
        j-=1
    j=col+1
    while(j<c-1 and trees[row, j]<trees[row, col]):
        rr+=1
        j+=1
    i=row-1
    while(i>0 and trees[i, col]<trees[row, col]):
        t+=1
        i-=1
    i=row+1
    while(i<r-1 and trees[i, col]<trees[row, col]):
        b+=1
        i+=1

    #print(l, rr, t, b)
    return l*rr*t*b

scores=[[score(row,col) for row in range(r)] for col in range(c)]
print(np.max(scores))
  