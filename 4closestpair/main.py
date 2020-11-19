#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:17:32 2020

@author: barre
"""
import math
import fileinput

def closest_points(p_list):
    
    px = sorted(p_list , key=lambda k: [k[0], k[1]])
    nbr_p = len(p_list)
    
    return closest(px,nbr_p)
    

def closest(p_x,n):
 #basfall 2 eller 3
    if n == 2:
        delta = pythagoras(p_x[0][0],p_x[1][0],p_x[0][1],p_x[1][1])
        return delta
        
    elif n == 3:
        d1 = pythagoras(p_x[0][0],p_x[1][0],p_x[0][1],p_x[1][1])
        d2 = pythagoras(p_x[0][0],p_x[2][0],p_x[0][1],p_x[2][1])
        d3 = pythagoras(p_x[1][0],p_x[2][0],p_x[1][1],p_x[2][1])
        delta = min(d1,d2,d3)
        return delta
        
    
    
    mid = math.ceil(n/2)
    
    l_x = p_x[:mid]
    r_x = p_x[mid:]
    
    delta_l = closest(l_x,len(l_x))
    delta_r = closest(r_x,len(r_x))
    
    delta = min(delta_l,delta_r)
    
    mid_x = p_x[mid][0]
    
    s_y = []
    temp_delta = delta +1
    
    for point in p_x:
        if point[0] >= (mid_x-delta) and point[0] <= (mid_x + delta):
            s_y.append(point)
    
            
    s_y = sorted(s_y , key=lambda k: [k[1], k[0]])
    
    for i in range(0,len(s_y)-1):
        
       # om punktens x är sörre än delta, kolla till vänster
        j = i +1
        
        if s_y[i][0]> mid_x:
            #fortsätt så länge nästa punkt är mindre än delta i y-led
            
            while s_y[j][1] - s_y[i][1] <  delta:
                #räkna dist
                d1 = pythagoras(s_y[i][0],s_y[j][0],s_y[i][1],s_y[j][1])
                if d1 < temp_delta:
                    temp_delta = d1
                
                j += 1
                if j == len(s_y):
                    break
                
                
        else:
            
            #samma som tidigare
            while s_y[j][1] - s_y[i][1] <  delta:
                d1 = pythagoras(s_y[i][0],s_y[j][0],s_y[i][1],s_y[j][1])
                if d1 < temp_delta:
                    temp_delta = d1
                
                j += 1
                if j == len(s_y):
                    break
                
            
    
    if temp_delta < delta:
        delta = temp_delta
    
    
    return delta


def pythagoras(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)



p_list = []


#contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/4closestpair/data/secret/2med.in").read()
#lines = [x.split(' ')for x in contents.split('\n')]
#[p_list.append([int(x[0]),int(x[1])]) for x in lines[1:-1]]
#



input_array = []
for line in fileinput.input():
    input_array.append(line.split(' '))


lines = []
for line in input_array[1:]:
    line[1] = line[1].rstrip('\n')
    lines.append(line)


[p_list.append([int(x[0]),int(x[1])]) for x in lines]




print("{:.6f}".format(closest_points(p_list)));
