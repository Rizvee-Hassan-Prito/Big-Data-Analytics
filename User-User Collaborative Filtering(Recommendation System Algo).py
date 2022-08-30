# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:50:25 2022

@author: User
"""
import numpy as np

m=[[4,1,0,4,0],[0,4,0,2,3],[0,1,0,4,4]]
m2=[[4,1,0,4,0],[0,4,0,2,3],[0,1,0,4,4]]

#%%
mean_list=[]
for i in range(len(m)):
  c=0
  for k in range(len(m[i])):
    if m[i][k]!=0:
        c+=1
  mean=sum(m[i])/c
  mean_list.append(mean)
  for j in range(len(m[i])):
    if m2[i][j]==0:
      m2[i][j]=mean   

print("\nUser Rating matrix with NULL : \n")
print(m)
print("\nUser Rating matrix replacing NULL using Mean user rating: \n")
print(m2)

#%%
import math

sim=[]

for k0 in range(len(m)-1):
  k=k0+1
  sim2=[]
  while(k<=(len(m)-1)):
    s1=[]
    s2=[]

    for j in range(len(m[k0])):
          if (m[k0][j]!=0 and m[k][j]!=0):
              s1.append(m[k0][j]-mean_list[k0])
              s2.append(m[k][j]-mean_list[k])
    
    sum=0 
    for i in range(0,len(s1)):
      sum+=s1[i]*s2[i]
    
    sq_sum1=0
    for i in range(0,len(s1)):
      sq_sum1+=s1[i]**2
    sq_sum1=math.sqrt(sq_sum1)
    
    sq_sum2=0
    for i in range(0,len(s2)):
      sq_sum2+=s2[i]**2
    sq_sum2=math.sqrt(sq_sum2)

    dnom = sq_sum1*sq_sum2
    
    simlarity=sum/dnom

    sim2.append(simlarity)
    k+=1

  
  sim.append(sim2)

print("\nUser Similarities for the matrix with Null: \n")
print(sim)

#%%
p=[]

for i in range(0,len(m)):
  pi=[]
  for j in range(0,len(m[i])):
    s1=[]
    for b in range(len(m)):
      if b!=i:
        s1.append(m[b][j])
    #print(s1)

    s2=[]
    for n in range(len(sim)):
      if(i==n):
        for n2 in range(len(sim[n])):
          s2.append(sim[n][n2])
      if(i-1<len(sim[n])):
          for n2 in range(len(sim[n])):
            if(n2==i-1):
               s2.append(sim[n][n2])
      if(i==len(m)-1):
        s2.append(sim[n-1][n2-1])
    #print(s2)

    sum=0
    sum2=0
    for s in range(len(s1)):
      sum+=s1[s]*s2[s]
      sum2+=s2[s]
    pi.append(sum/sum2)
  p.append(pi)

print("\nPrediction Matrix for the matrix with Null: \n")
p=np.array(p)
print(p)

#%%

sim=[]
for k0 in range(len(m2)-1):
  k=k0+1
  sim2=[]
  while(k<=(len(m2)-1)):
    s1=[]
    s2=[]

    for j in range(len(m[k0])):
          if (m2[k0][j]!=0 and m2[k][j]!=0):
              s1.append(m2[k0][j]-mean_list[k0])
              s2.append(m2[k][j]-mean_list[k])
    
    sum=0 
    for i in range(0,len(s1)):
      sum+=s1[i]*s2[i]
    
    sq_sum1=0
    for i in range(0,len(s1)):
      sq_sum1+=s1[i]**2
    sq_sum1=math.sqrt(sq_sum1)
    
    sq_sum2=0
    for i in range(0,len(s2)):
      sq_sum2+=s2[i]**2
    sq_sum2=math.sqrt(sq_sum2)

    dnom = sq_sum1*sq_sum2
    
    simlarity=sum/dnom

    sim2.append(simlarity)
    k+=1

  
  sim.append(sim2)
print("\nUser Similarities for the matrix with Mean user rating: \n")
print(sim)

#%%

p=[]

for i in range(0,len(m2)):
  pi=[]
  for j in range(0,len(m2[i])):
    s1=[]
    for b in range(len(m2)):
      if b!=i:
        s1.append(m2[b][j])
    #print(s1)

    s2=[]
    for n in range(len(sim)):
      if(i==n):
        for n2 in range(len(sim[n])):
          s2.append(sim[n][n2])
      if(i-1<len(sim[n])):
          for n2 in range(len(sim[n])):
            if(n2==i-1):
               s2.append(sim[n][n2])
      if(i==len(m2)-1):
        s2.append(sim[n-1][n2-1])
    #print(s2)

    sum=0
    sum2=0
    for s in range(len(s1)):
      sum+=s1[s]*s2[s]
      sum2+=s2[s]
    pi.append(sum/sum2)
  p.append(pi)

print("\nPrediction Matrix for the matrix with Mean user rating: \n")
p=np.array(p)
print(p)
#%%
nor_mat=[]
n0=0
for i in p:
    n1=0
    nor_m=[]
    for j in i:
        max=j
        min=j
        for k in i:
            if(k>max):
                max=k
        
        for k in i:
            if(k<min):
                min=k
        
        nor_m.append((j-min)/(max-min))
        n1+=1
    nor_mat.append(nor_m)
    n0+=1

print("\nNormalized Prediction Matrix: \n")
nor_mat=np.array(nor_mat)
print(nor_mat)
