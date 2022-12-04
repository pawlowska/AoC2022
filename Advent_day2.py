# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:35:42 2022

@author: Monik
"""

import pandas as pd

wynik=pd.DataFrame({'A': [3, 6, 0],
                   'B': [0, 3, 6],
                   'C': [6, 0, 3]}, index=['R', 'P', 'S'])


dic_part1={'X':'R', 'Y': 'P', 'Z':'S'}
#was part1 12855
dic_part2={'X':0, 'Y': 3, 'Z':6}

with open('day2_input.txt') as f:
    lines=f.readlines()

# temp=['A Y', 'B X', 'C Z']

def score1(l):
    """
    score for is score for shape (1 Rock X, 2 Paper Y, and 3 Scissors Z) 
    plus score for outcome (0 if  lost, 3 if draw, and 6 if  won).
    """
    them=l[0]
    me=dic_part1[l[2]]
    return wynik[them][me]+wynik.index.get_loc(me)+1
    

all_scores1=[score1(l) for l in lines]    
    
print(sum(all_scores1))

def score2(l):
    """
    the second column says how the round needs to end: 
    X you lose, Y you draw, and Z you win
    """
    them=l[0]
    me=dic_part2[l[2]]
    return me+pd.Index(wynik[them]).get_loc(me)+1

print(sum([score2(l) for l in lines]))