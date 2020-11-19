#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import fileinput

from methods import GS, MakeInvertedListWoman, MakeFifoQueueMan

start_time = time.time()
inputArray = []

# reads the input file into a list
for line in fileinput.input():
    a = line.split(' ')
    for x in a:
        inputArray.append(int(x))



#
#time_1 = time.time()

#creates sets of men and women
W = dict()
M = dict()



# takes the first element as number of people
nbrPersons = int(inputArray[0])
indexSeen = []

    # puts the men and women into sets, checks the index if its a man or a woman
for i in range(1,len(inputArray)-1,nbrPersons+1):
    
    prefList = inputArray[i+1:i+nbrPersons+1]
    index = inputArray[i]
    
    #kön
    
    
    if index in indexSeen:
        M[index] = MakeFifoQueueMan(prefList)
    # lägger in kvinnor    
    else:
        indexSeen.append(index)   
        W[index] = MakeInvertedListWoman(prefList)
    
##    
#time_2 = time.time()

res = GS(W,M)
output = []
for i in range(1,len(res)+1):
    print(res[i])

#
#print('tid för inläsning:' + str(time_1-start_time))
#print('tid för lägga in i listor och köer:' + str(time_2-time_1))
#print('tid för GS:' + str(time.time()-time_2))