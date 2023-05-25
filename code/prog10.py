# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:01:04 2023

@author: 91990
"""
check=None
i=0
c=0
avg=0
while i!="*":
    i=input("enter the no")
    n=i
    if n<i:
        print(f"the largest no is {i}")
    else:
        print(f"the largest no is {n}")
    sum=sum+i
    c=c+1
    avg=sum/c
    print(f"the avg is {i}")  
    