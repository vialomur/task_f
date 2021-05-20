# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:10:07 2021

@author: administrator
"""
import sys

c1,c2,c3 = map(int, input().split())
k1,k2,k3 = map(int, input().split())
n = int(input())
count = 0
diction = {k1:c1,k2:c2,k3:c3}
list_d = list(diction.items())
list_d.sort(key=lambda i: i[1])
k1_t,k2_t,k3_t = list_d[0][0],list_d[1][0],list_d[2][0]
c1_t,c2_t,c3_t = list_d[0][1],list_d[1][1],list_d[2][1]
print(k1_t,k2_t,k3_t)
print(c1_t,c2_t,c3_t)

while k1_t > 0:
    if n <= 0:
        print(count)
        sys.exit()
    n -= c1_t
    k1_t -= 1
    count += 1
    if n < c1_t:
        break
while k2_t > 0:
    if n <= 0:
        print(count)
        sys.exit()
    n -= c2_t
    k2_t -= 1
    count += 1
    if n < c2_t:
        break
while k3_t > 0:
    if n <= 0:
        print(count)
        sys.exit()
    n -= c3_t
    k3_t -= 1
    count += 1
    if n < c3_t:
        print(count)
        sys.exit()
print(count)
