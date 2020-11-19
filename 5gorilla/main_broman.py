import fileinput
import numpy as np
import sys
sys.setrecursionlimit(10000)

def OPT(string_i,string_j):
    
    #Vikten finns, ta reda på vilket ord det är och returnera.
    if len(string_i) > 0 and len(string_j) > 0 and weights[len(string_i)-1][len(string_j)-1] > -10000:
        return [words[len(string_i)-1][len(string_j)-1][0],words[len(string_i)-1][len(string_j)-1][1], weights[len(string_i)-1][len(string_j)-1]]
    
    # Basfall
    if string_i == '':
        weights[len(string_i)-1][len(string_j)-1] = len(string_j)*delta
        words[len(string_i)-1][len(string_j)-1][0] = len(string_j)*'*'
        words[len(string_i)-1][len(string_j)-1][1] = string_j
        return [len(string_j)*'*', string_j, len(string_j)*delta]
    if string_j == '':
        weights[len(string_i)-1][len(string_j)-1] = len(string_i)*delta
        words[len(string_i)-1][len(string_j)-1][0] = string_i
        words[len(string_i)-1][len(string_j)-1][1] = len(string_i)*'*'
        return [string_i,len(string_i)*'*',len(string_i)*delta]
    
    #fall 1:
    new_weight = int(w_matrix[letters_dict.get(string_i[-1])][letters_dict.get(string_j[-1])])
    
    [str_i_1,str_j_1, delta1] = OPT(string_i[:-1],string_j[:-1])
    [str_i_2,str_j_2, delta2] = OPT(string_i,string_j[:-1])
    [str_i_3,str_j_3, delta3] = OPT(string_i[:-1],string_j)
    
    if delta1 + new_weight >= (delta2+delta) and delta1 + new_weight >= (delta3+delta):
        weights[len(string_i)-1][len(string_j)-1] = delta1+new_weight
        words[len(string_i)-1][len(string_j)-1][0] = str_i_1 +string_i[-1]
        words[len(string_i)-1][len(string_j)-1][1] = str_j_1 + string_j[-1]
        return [str_i_1 + string_i[-1],str_j_1 + string_j[-1],delta1+new_weight]
        
    elif delta2 + delta > (delta1 + new_weight) and delta2 + delta > (delta3+delta):
        weights[len(string_i)-1][len(string_j)-1] =delta2+delta
        words[len(string_i)-1][len(string_j)-1][0] = str_i_2 + '*'
        words[len(string_i)-1][len(string_j)-1][1] = str_j_2 + string_j[-1]
        return [str_i_2 + '*',str_j_2 + string_j[-1],delta2+delta]
    else:
        weights[len(string_i)-1][len(string_j)-1] =delta3+delta
        words[len(string_i)-1][len(string_j)-1][0] = str_i_3 + string_i[-1]
        words[len(string_i)-1][len(string_j)-1][1] = str_j_3 + '*'
        return [str_i_3 + string_i[-1],str_j_3 + '*',delta3+delta]
        
    
p_list = []

#================ LÄS IN DATA ==================
#lines = []
#for line in fileinput.input():
#    line = line.replace('\n', '')
#    lines.append(line.split(' '))
#
#letters = lines[0]
#nbr_chr = len(letters)
#
#delta = -4
#w_temp = []
#[w_temp.extend(line) for line in lines[1:nbr_chr+1]]
#w_matrix = []
#for i in range(0,nbr_chr):
#    w_matrix.append(w_temp[(i*nbr_chr):((i+1)*nbr_chr)])
#
#nbr_q = int(lines[nbr_chr + 1][0])
#
#q_matrix = []
#[q_matrix.append(line) for line in lines[(nbr_chr+2):]]

#===============================================



#======= MANUELL INLÄSNING AV DATA =============
contents = open("/Users/barre/Desktop/EDAF05-labs-public-master//5gorilla/data/secret/3large.in").read()
lines = [x.split(' ')for x in contents.split('\n')]

delta = -4
letters  = lines[0];
nbr_chr = len(letters)
w_temp = []
[w_temp.extend(line) for line in lines[1:nbr_chr+1]]
w_matrix = []
for i in range(0,nbr_chr):
    w_matrix.append(w_temp[(i*nbr_chr):((i+1)*nbr_chr)])
nbr_q = int(lines[nbr_chr + 1][0])
q_matrix = []
[q_matrix.append(line) for line in lines[(nbr_chr+2):-1]]

#===============================================

letters_dict = {}
for c in range(len(letters)):
    letters_dict[letters[c]]=c
    
weights = []
words = []

string1 = ''
string2 = ''
for n in range(nbr_q):
    string1 = q_matrix[n][0]
    string2 = q_matrix[n][1]
    cols = len(string2) + 1
    rows = len(string1) + 1
    a = np.ones((rows,cols))*(-99999)
    weights = a.astype(int)
    words = [[['',''] for c in range(cols)] for r in range(rows)]
    print(OPT(string1,string2)[0] + ' ' + OPT(string1,string2)[1] )