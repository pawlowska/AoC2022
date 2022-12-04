# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:38:29 2022

@author: Monik
"""

# %% load data

with open('day3_input.txt') as f:
    lines=f.readlines()

# %% define functions
def szukaj_duplikatu(s1, s2): 
    rzecz=set(s1) & set(s2) #intersect two sets
    return(list(rzecz)) #convert set to list

def priorytet(c):
    if(ord(c) in range(ord('a'), ord('z')+1)):
       return ord(c)+1-ord('a')
    elif(ord(c) in range(ord('A'), ord('Z')+1)):
       return ord(c)+27-ord('A')
    else:
       return 0

def badge(trzy):
    pierwsze=szukaj_duplikatu(trzy[0][:-1], trzy[1][:-1]) #-1 for ignoring the end line symbol
    b=szukaj_duplikatu(pierwsze, trzy[2])
    return(b[0]) #assume that b has one element
    
# %% part 1
rzeczy=[szukaj_duplikatu(l[0:len(l)//2], l[len(l)//2:]) for l in lines]
punkty1=[priorytet(r[0]) for r in rzeczy]
print(sum(punkty1))

# %% part2

badges=[badge(lines[3*i:3*i+3]) for i in range(len(lines)//3)]
punkty2=[priorytet(r[0]) for r in badges]

print(sum(punkty2))
