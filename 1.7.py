#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def zero(mat):
    N=len(mat)
    M=len(mat[0])
    Ncheck=[True for index in range(N)]
    Mcheck=[True for index in range(M)]

    for x in range(M):
        for y in range(N):
            if mat[y][x]==0:
                Ncheck[y]=0
                Mcheck[x]=0

    for x in range(M):
        for y in range(N):
            if Ncheck[y] * Mcheck[x]==0:
                mat[y][x]=0
                
    return mat

mat1=[[0,  2, 3, 4, 5, 6],
      [7,  8, 9,10,11,12],
      [13,14,15,16,17,18],
      [19,20,21,22,23,24],
      [25,26,27, 0,29,30],
      [31,32,33,34,35,36],
      [37,38,39,40,41,42]]
print(zero(mat1))


