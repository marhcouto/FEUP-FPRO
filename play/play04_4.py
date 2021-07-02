# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:39:22 2019

@author: marhc
"""

def get_positions(sentence, word_list):
    alist1 = sentence.split()
    for i in range(len(alist1)):
        if alist1[i] in word_list:
            for n in range(len(word_list)):
                if alist1[i] == word_list[n]:
                    alist1[i] = n
    alist1 = list(filter(lambda a: type(a) is int, alist1))
    if len(alist1) == 0:
        return ""
    alist1 = list(map(lambda a: str(a), alist1))
    answer = (" ").join(alist1)
    return answer
                

print(get_positions('hello world hello', ['hello', 'world', 'lousy']))

                
    
            