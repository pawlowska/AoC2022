# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:58:41 2022

@author: Monik
"""
#%%
def process_stack_level(lev_raw, n):
    return [lev_raw[i*4: i*4+3] for i in range(n)]
    
def process_move(m_raw):
    m=m_raw.split()
    print()
    return int(m[1]), int(m[3]), int(m[5])
    

# %% load data

f_test='day5_test.txt'
f_in='day5_input.txt'

with open(f_in) as f:
    lines=f.readlines()
    
split=0
while(len(lines[split])>1):
    split=split+1
    
stacks_raw=lines[0:split-1]

nstacks=(len(stacks_raw[-1])+1)//4
allstacks= [ [] for _ in range(nstacks) ]

for j in range(len(stacks_raw)-1, -1, -1):
    lev=process_stack_level(stacks_raw[j], nstacks)
    for i in range(len(lev)):
        if lev[i]!='   ':
            allstacks[i].append(lev[i])
        
print(allstacks)
    

# %% do moves part1
moves=lines[split+1:]

for m in moves:
    k, st1, st2 = process_move(m)
    for i in range(k):
        obj=allstacks[st1-1].pop()
        allstacks[st2-1].append(obj)
        
#print(allstacks)
# %% do moves part2
moves=lines[split+1:]

for m in moves:
    k, st1, st2 = process_move(m)
    ind1, ind2=st1-1, st2-1
    p=len(allstacks[ind1])-k
    for i in range(k):
        obj=allstacks[ind1].pop(p)
        print(obj)
        allstacks[ind2].append(obj)
# %% print
res=""
for s in range(nstacks):
    top_obj=allstacks[s][-1]
    res+=top_obj[1]
    
print(res)