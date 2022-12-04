# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 06:49:36 2022

@author: Monik
"""

with open('day1_input.txt') as f:
    lines=f.readlines()

lines.append('\n')    
lista=[]

suma=0

for i in range(len(lines)):
    l=lines[i]
    if(l=='\n'):
        lista.append(suma)
        suma=0
    else:
        suma=suma+int(l)


nowa_lista=[]

for i in range(3):
    m=lista.pop(lista.index(max(lista)))
    print(m)
    nowa_lista.append(m)
    
print(sum(nowa_lista))
    