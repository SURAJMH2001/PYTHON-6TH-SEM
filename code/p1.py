# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:45:51 2023

@author: 91990
"""

def remove(os,ss):
    if ss in os:
        return os.replace(ss,"")
    else:
        return os
    
os=input()
ss=input()
result=remove(os,ss)
print(result)