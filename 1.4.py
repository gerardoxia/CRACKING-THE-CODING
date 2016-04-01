#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def WhetherAnagrams(str1,str2):
    check = [] ## 防止被骂 下面设置下长度和类型
    for ListGenerateIndex in range(256):
        check.append(0)        
    length1=len(str1)
    length2=len(str2)
    if length1 != length2: return False
    for index in str1:
        asciiNum1 = ord(index)
        check[asciiNum1] = check[asciiNum1]+1
    for index in str2:
        asciiNum2 = ord(index)
        check[asciiNum2] = check[asciiNum2]-1
    for index in check:
        if index != 0: return False
        

    return True


str1='abcdewwa'
str2='aabwwcde'
print(WhetherAnagrams(str1,str2))


