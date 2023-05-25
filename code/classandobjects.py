# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:23:50 2023

@author: 91990
"""

class student:
    def __init__(self,name,cgpa=0.0,usn=0):
        self.name=name
        self.cgpa=cgpa
        self.usn=usn
        print(f"Welcome to EEE department {self.name} ,{self.usn},{self.cgpa}")
       
    def allcusn(self,usn):
        self.usn=usn
        
    def allccgpa(self,cgpa):
        self.cgpa=cgpa
       
    def display(self):
        print("Name:",self.name)
        print("USN:",self.usn)
        print("CGPA:",self.cgpa)
        
def find_larger(s1,s2):
    if s1.cgpa>s2.cgpa:
        print(s1.name)
    else:
        print(s2.name)
        
print("Enter the details")
name=input()
s1=student(name)

usn=input("enter the usn")     
s1.allcusn(usn)

cgpa=input("enter the cgpa")
s1.allccgpa(cgpa)

s1.display()
s1=student(name,cgpa,usn)


name=input()
s2=student()

usn=input()
s2.allcusn(usn)     

cgpa=int(input()) 
s2.allccgpa(cgpa)

s2.display()
s2=student(name,cgpa,usn)


a=find_larger(s1, s2)

