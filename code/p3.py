# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:52:52 2023

@author: 91990
"""

def rrc(ips):
    pc=""
    currcharcnt=1
    ops=""
    for char in ips:
        if char==pc:
            currcharcnt+=1
            if currcharcnt==3:
                ops=ops[:-1]+" "
                
        else:
            currcharcnt=1
        
        ops+=char
        pc=char
    return ops
ips=input()
result=rrc(ips)
print(result)