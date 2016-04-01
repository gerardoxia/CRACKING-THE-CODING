#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def rotate(pic):
    N=len(pic)
    for x in range(N):
        for y in range(N):
            if x<=y:
                temp=pic[x][y]
                pic[x][y]=pic[y][x]
                pic[y][x]=temp
    for index in range(N//2):
        for y in range(N):
            temp=pic[index][y]
            pic[index][y]=pic[N-1-index][y]
            pic[N-1-index][y]=temp
    return pic

pic1=[[1,2,3,4,5,6],
      [7,8,9,10,11,12],
      [13,14,15,16,17,18],
      [19,20,21,22,23,24],
      [25,26,27,28,29,30],
      [31,32,33,34,35,36]]
print(rotate(pic1))


