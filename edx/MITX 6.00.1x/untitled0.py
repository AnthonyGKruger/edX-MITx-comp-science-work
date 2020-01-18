#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 04:58:16 2018

@author: anthony
"""
s = 'azcbobobegghakl'
boblength = len('abcdefghijklmnopqrstuvwxyz')
total = 0
for char in range(len(s)):
    if s[char : char + boblength] == 'abcdefghijklmnopqrstuvwxyz':  
        total += 1
print('Number of times bob occurs is:' + str(total))


prev_substring = ''
cur_substring = ''
long_substring = ''
for char in s:
    if prev_substring <= char:
        cur_substring += char
        if len(cur_substring) > len(long_substring):
            long_substring = cur_substring
    else:
        cur_substring = char
    prev_substring = char

print('Longest substring in alphabetical order is: '+ long_substring)
