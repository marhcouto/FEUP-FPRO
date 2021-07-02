# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:11:47 2019

@author: marhc
"""

def longest(s):
    s_list = s.split()
    length_s_list = []
    print(s_list)
    for word in s_list:
        length_s_list.append(len(word))
        print(length_s_list)
    longest = max(length_s_list)
    return longest

print(longest('Unnecessarily long sentence since the longest word is the first one'))
        