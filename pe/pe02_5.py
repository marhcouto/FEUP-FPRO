# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:21:04 2019

@author: marhc
"""

def exactly(s):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    pair = ""
    pairs = ()
    stop = False
    no = 0
    s_list = list(s)
    for n1 in s:
        if n1 in numbers:
            s_list.remove(n1)
            for n2 in s_list:
                if n2 in numbers:
                    pair_sum = int(n1) + int(n2)
                    if pair_sum == 10:
                        pair = n1 + n2
                        pairs = pairs + (pair,)
                        for quest_mark in s[s.find(n1):s.find(n2)]:
                            if quest_mark == "?":
                                no += 1
                        if no != 3:
                            return str("The sequence " + s + " is NOT OK with first violation with pair:" + str(pairs))
                            stop = True
                            break
                if stop:
                    break
        if stop:
            break
    return str("The sequence " + s + " is OK with the pairs:" + str(pairs))
                        
                        
                    

print(exactly('htrtr24?h56h56??29004??34'))