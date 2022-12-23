# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:14:50 2022

@author: Monik
"""

# %% load data

f_test='day7_test.txt'
f_in='day7_input.txt'

with open(f_in) as f:
    lines=f.readlines()
    
 
# %%

i=0

sizes={}
parents=[]

while(i<len(lines)):
    l=lines[i].split()
    if (l[0:2]==['$', 'cd']):
        el=l[2]
        if el=='..': #last dir finished, remove
            parents.pop(-1) 
        else: #new dir discovered
            el=el+str(i)
            parents.append(el) #this dir will be counted as parent for following files
            sizes[el]= 0
    elif l[0].isnumeric(): #file discovered
        for p in parents:
            sizes[p]=sizes[p]+int(l[0]) #add file size to all 'open' dirs
    i+=1

# %%    

suma=0

for d in sizes:
    s=sizes[d]
    if(s<=100000):
        suma=suma+s
        
print(suma)

# %%

fs=70000000
free=fs-sizes['/0']
needed=30000000-free

delete=30000000

for d in sizes:
    s=sizes[d]
    if(s>needed and s<delete):
        delete=s
        
print(delete)
    