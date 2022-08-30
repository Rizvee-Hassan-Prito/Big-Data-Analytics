# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 00:02:11 2022

@author: User
"""

n = int(input("Number of Pages:"))

Matrix = []
print("Enter 1 for InLinks:")
for i in range(0,n):
  x=[]
  for j in range(0,n):
    x.append(int(input("Enter:")))
  Matrix.append(x)
  print("Enter 1 for next Page's InLinks:")

print(Matrix)
#%%
Num_of_InLinks_Pages =[]
for j in range(0,n):
    sum=0
    for i in range(0,n):
      sum+= Matrix[i][j]
    Num_of_InLinks_Pages.append(sum)

print(Num_of_InLinks_Pages)
#%%
M =[]
for i in range(0,n):
    x=[]
    for j in range(0,n):
      if (Matrix[i][j]==1):
        x.append(1/Num_of_InLinks_Pages[j])
      else:
         x.append(0)
    M.append(x)
print(M)
#%%
r0=[]
for i in range(0,n):
  x=[]
  for j in range(0,n):
    x.append(1/n)
  r0.append(x)

print(r0)
#%%
B_M=[]
for i in range(0,n):
  x=[]
  for j in range(0,n):
    x.append(0.9*M[i][j])
  B_M.append(x)

one_B_R0=[]
for i in range(0,n):
  x=[]
  for j in range(0,n):
    x.append(0.1*r0[i][j])
  one_B_R0.append(x)

A=[]
for i in range(0,n):
  x=[]
  for j in range(0,n):
    x.append(B_M[i][j]+one_B_R0[i][j])
  A.append(x)
print(A)
#%%
r00=[]
for j in range(0,n):
    r00.append(r0[0][j])
print(r00)
#%%
import numpy as np

result=np.array(r00)
A= np.array(A)
n= int(input("Enter the number of iteration:"))
z=0
while(z!=n):
  r=result 
  result= np.dot(A,result)
  z+=1
print("Matrix r:\n",result)