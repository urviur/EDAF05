#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:17:32 2020

@author: barre
"""

import math
import fileinput



#
#def OPT(i,j):
#    if i == 0:
#        return j*delta
#    if j == 0:
#        return i*delta
#    
#    delta1 = int(w_matrix[letters_dict.get(string1[i-1])][letters_dict.get(string2[j-1])]) + OPT(i-1,j-1)
#    delta2 = delta + OPT(i,j-1)
#    delta3 = delta + OPT(i-1,j)
#    
#    temp_delta = max(delta1,delta2,delta3)
#    
#    return temp_delta




def OPT(string_i,string_j):
    if string_i == '':
        return [len(string_j)*'*',string_j, len(string_j)*delta]
    if string_j == '':
        return [string_i,len(string_i)*'*',len(string_i)*delta]
    
    #fall 1:
    new_weight = int(w_matrix[letters_dict.get(string_i[-1])][letters_dict.get(string_j[-1])])
    
    [str_i_1,str_j_1, delta1] = OPT(string_i[:-1],string_j[:-1])
    [str_i_2,str_j_2, delta2] = OPT(string_i,string_j[:-1])
    [str_i_3,str_j_3, delta3] = OPT(string_i[:-1],string_j)
    
    if delta1 + new_weight >= (delta2+delta) and delta1 + new_weight >= (delta3+delta):
        return [str_i_1 + string_i[-1],str_j_1 + string_j[-1],delta1+new_weight]
        
    elif delta2 + delta > (delta1 + new_weight) and delta2 + delta > (delta3+delta):
        return [str_i_2 + '*',str_j_2 + string_j[-1],delta2+delta]
    else:
        return [str_i_3 + string_i[-1],str_j_3 + '*',delta3+delta]
        
        
    




p_list = []



contents = open("//Users/barre/Desktop/EDAF05-labs-public-master/5gorilla/data/secret/3small.in").read()
lines = [x.split(' ')for x in contents.split('\n')]
#[p_list.append([int(x[0]),int(x[1])]) for x in lines[1:-1]]

delta = -4
letters  = lines[0];
nbr_chr = len(letters)
w_matrix = []
[w_matrix.append(line) for line in lines[1:(nbr_chr+1)]]

nbr_q = int(lines[nbr_chr + 1][0])
q_matrix = []
[q_matrix.append(line) for line in lines[(nbr_chr+2):-1]]


letters_dict = {}
for c in range(len(letters)):
    letters_dict[letters[c]]=c
m = []

for n in range(nbr_q):
    string1 = q_matrix[n][0]
    string2 = q_matrix[n][1]
    print(OPT(string1,string2))




#input_array = []
#for line in fileinput.input():
#    input_array.append(line.split(' '))
#
#
#lines = []
#for line in input_array[1:]:
#    line[1] = line[1].rstrip('\n')
#    lines.append(line)
