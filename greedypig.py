#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:47:02 2022

@author: radhakrishna


This program measures the counts for a set of integers to solve

a1+a2+a3+a4... > X

Rference being greedy pig problem on Number phile.

We can obviously work with cartesian product but it's going to kill the time,
So we do combinations with replacement and manually add the cases with comb 
function for probabilites.

"""

from itertools import combinations_with_replacement
from math import comb
import matplotlib.pyplot as plt

def reach_score_in_rolls(score,rolls):
    possibilities=0
    available=[2,3,4,5,6]
    ar=[]
    for game in combinations_with_replacement(available, rolls):
        if sum(game)>=score:
            ar.append(game)
            possibilities+=perm_of_comb(game)
    return possibilities/(6**rolls),ar

def perm_of_comb(ar):
    group={}
    for el in ar:
        try:
            group[el]+=1
        except:
            group[el]=1
    N=len(ar)#total_numbers
    G=group.keys()#number of groups
    '''
    Treat each group length as different combination set
    so for [6,6,2,2,5] we have to place 2 6s, 2 2s, 1 5 so
    
    5c2*3c2*1 or 5c1*4c2 = 30/(6**5) probability for this particular
    
    combination to occur
    
    '''
    product=1
    for g in G:
        product*=comb(N,group[g])
        N-=group[g]
    return product
''' 
Plot different curves for different rolls.

Plot probability for different scores in each curve.

'''
rolls_data=[]
for rolls in range(2,9): # for every roll,
    print(f"Calculating for rolls = {rolls}")
    score_data=[]
    for score in range(2,30): #probability for every score of a given score
        prob,posb=reach_score_in_rolls(score,rolls)
        score_data.append(prob)
    rolls_data.append(score_data)
i=2
for data in rolls_data:
    plt.plot(list(range(2,30)),data,label=f"ROll curve : {i}")
    i+=1

plt.legend(loc="upper right")

