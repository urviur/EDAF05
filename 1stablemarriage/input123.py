#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:29:08 2020

@author: barre
"""

import sys
 
inp_file = sys.argv[1]

contents = open(inp_file).read()

tempString = contents.split('\n')

tempString = ' '.join(tempString)
inputArray = tempString.split(' ')

print(inputArray)