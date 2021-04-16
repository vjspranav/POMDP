#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:27:43 2021

@author: vjspranav
"""

import math 

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

rollnum=2020121001
x = 1 - ((int(str(rollnum)[-4:]) % 30) + 1)/100
y = ((int(str(rollnum)[-2:]) % 4) + 1)

table = [
    {
     "RED" : {
        "RED" : 0.95,
        "GREEN": 0.05
        },
    "GREEN" :{
        "RED" : 0.2,
        "GREEN": 0.8
            }
    },
    {
     "RED" : {
        "RED" : 0.9,
        "GREEN": 0.1
        },
    "GREEN" :{
        "RED" : 0.15,
        "GREEN": 0.85
        }
    },{
     "RED" : {
        "RED" : 0.85,
        "GREEN": 0.15
        },
    "GREEN" :{
        "RED" : 0.1,
        "GREEN": 0.9    
       },
    },
    {
     "RED" : {
        "RED" : 0.8,
        "GREEN": 0.2
        },
    "GREEN" :{
        "RED" : 0.05,    
        "GREEN": 0.95    
       },
    }
]

Ps = table[y-1]
Pa = {
      1 : x,
      0 : 1-x
      }

states = ["S1", "S2", "S3", "S4", "S5", "S6"]
colors = ["RED", "GREEN", "RED", "GREEN", "GREEN", "RED"]

B = [1/3, 0, 1/3, 0, 0, 1/3]
U=[]
X={}

u=[]
color = "GREEN"
for i in range(6):
    if i==0:
        u.append(Ps[colors[i]][color] * ((Pa[0] * B[i]) + (Pa[0] * B[i+1])))    
    elif i==5:
        u.append(Ps[colors[i]][color] * ((Pa[1] * B[i-1]) + (Pa[1] * B[i])))
    else:
        u.append(Ps[colors[i]][color] * ((Pa[1] * B[i-1]) + (Pa[0] * B[i+1])))
    
b = [[i/sum(u) for i in u]]

B = [i for i in b[0]]
u=[]
color = "RED"
for i in range(6):
    if i==0:
        u.append(Ps[colors[i]][color] * ((Pa[1] * B[i]) + (Pa[1] * B[i+1])))
    elif i==5:
        u.append(Ps[colors[i]][color] * ((Pa[0] * B[i-1]) + (Pa[0] * B[i])))
    else:
        u.append(Ps[colors[i]][color] * ((Pa[0] * B[i-1]) + (Pa[1] * B[i+1])))
    
b.append([i/sum(u) for i in u])

B = [i for i in b[1]]
u=[]
color = "GREEN"
for i in range(6):
    if i==0:
        u.append(Ps[colors[i]][color] * ((Pa[1] * B[i]) + (Pa[1] * B[i+1])))
    elif i==5:
        u.append(Ps[colors[i]][color] * ((Pa[0] * B[i-1]) + (Pa[0] * B[i])))
    else:
        u.append(Ps[colors[i]][color] * ((Pa[0] * B[i-1]) + (Pa[1] * B[i+1])))
b.append([i/sum(u) for i in u])

s="2020121001 2020121003\n" + str(x) + " " + str(y) + "\n"
for i in b:
    for j in i:
        s+=str(truncate(j, 4)) + " "
    s += "\n"

with open("2020121001_2020121003.txt", "a") as f:
        f.write(s)

# Right and Green
#u1 = Ps["RED"]["GREEN"] * ((Pa[0] * B[0]) + (Pa[0] * B[1]))
#u2 = Ps["GREEN"]["GREEN"] * ((Pa[1] * B[0]) + (Pa[0] * B[2]))
#u3 = Ps["RED"]["GREEN"] * ((Pa[1] * B[1]) + (Pa[0] * B[3]))
#u4 = Ps["GREEN"]["GREEN"] * ((Pa[1] * B[2]) + (Pa[0] * B[4]))
#u5 = Ps["GREEN"]["GREEN"] * ((Pa[1] * B[3]) + (Pa[0] * B[5]))
#u6 = Ps["RED"]["GREEN"] * ((Pa[1] * B[4]) + (Pa[1] * B[5]))
#U = [u1, u2, u3, u4, u5, u6]
#X["1"] = {"U" : U[:]} 

#b = [B]
#b = [[i/sum(U) for i in U]]

