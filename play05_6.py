# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:46:31 2019

@author: marhc
"""

def removal(string, character):
    return (string[0:string.find(character)] + string[string.find(character) + 1:])    


def palyndrome_index(s):
    if s == s[::-1]:
        return (-1)
    else:
        for char in s:
            if (removal(s, char)) == (removal(s, char))[::-1]:
                return s.index(char)
        else:
            return (-1)
        
        
print(palyndrome_index("aaab"))
    