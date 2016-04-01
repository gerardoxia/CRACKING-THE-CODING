#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def isSubstring(str1,str2):
    length1=len(str1)
    length2=len(str2)
    check=True
    if length1>length2: return False

    for index2 in range(length2-length1+1):
        index=index2-1

        for index1 in range(length1):
            index=index+1
            if str1[index1]!=str2[index]:
                check=False
                break
            check=True
        if check==True: break
                
    return check

def isRotation(str1,str2):
    str3=str2+str2
    return(isSubstring(str1,str3))

str1='waterbottle'
str2='erbottlewate'

print(isRotation(str1,str2))

