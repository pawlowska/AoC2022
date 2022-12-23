# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 07:43:17 2022

@author: Monik
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:40:25 2022

@author: Monik
"""

import numpy as np

drcs={'R':np.array([ 1, 0]),
      'L':np.array([-1, 0]),
      'U':np.array([ 0, 1,]),
      'D':np.array([ 0, -1])}

def move_to_vector(l):
    drc, val = l.split()
    v=np.tile(drcs[drc], (int(val), 1))
    return v

def do_move(H, T, m):
    H=H+m
    diff=H-T
    dist=np.linalg.norm(diff)
    if dist==1 or dist==np.sqrt(2):
        T=T  #tail can stay
    elif dist==2:
        T=T+m #tail has to follow
    else:
        new_m=(np.sign(diff[0]), np. sign(diff[1]))
        T=T+new_m
    return H, T

def draw(positions, symbol='#'):
    max0, max1=np.max(positions, axis=0)
    min0, min1=np.min(positions, axis=0)
    print()
    canvas=np.full((max0-min0+1, max1-min1+1), '.')
    for p in positions:
        canvas[p[0]-min0, p[1]-min1]=symbol
    canvas=np.transpose(canvas)
    for i in range(canvas.shape[0]-1,-1, -1):
        print(''.join(canvas[i,:]))
# %% load data

f_test='day9_test.txt'
f_test2='day9_test2.txt'
f_in='day9_input.txt'

with open(f_in) as f:
    lines=f.readlines()

moves=np.concatenate([move_to_vector(l) for l in lines])

#%%

H=[0,0]
T=[0,0]
#heads=np.array([H])
tails=np.array([T])

for m in moves:
    H, T=do_move(H, T, m)
    tails=np.vstack((tails, T))

tails_unique=np.unique(tails, axis=0)
print(tails_unique.shape[0])


#%%
init=np.tile([0,0], (10, 1))

result=np.tile([0,0], (10, 1))

for m in moves:
    mov=m
    init[0]=init[0]+mov
    for i in range(1, len(init)):
        diff=init[i-1]-init[i]
        dist=np.linalg.norm(diff)
        if dist==1 or dist==np.sqrt(2):
            mov=[0,0] #tail can stay
        else:
            mov=(np.sign(diff[0]), np. sign(diff[1]))
        init[i]=init[i]+mov
    result=np.dstack((result, init))

#%%
def draw_state(s):
    positions=result[:,:,s]
    max0, max1=5, 8 #np.max(positions, axis=0)
    min0, min1=-12, -12 #np.min(positions, axis=0)
    canvas=np.full((max0-min0+1, max1-min1+1), '.')
    canvas[-min0,-min1]='s'
    for i in range(10):
        canvas[positions[i][0]-min0, positions[i][1]-min1]=str(i)
    canvas=np.transpose(canvas)

    for i in range(canvas.shape[0]-1,-1, -1):
        print(''.join(canvas[i,:]))
    print('')

draw_state(13)
draw_state(13+8)
draw_state(13+8+3)
#%%
tail=np.transpose(result[9,:,:])
#draw(tail)
print(np.unique(tail, axis=0).shape[0])

