# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:14:43 2019

@author: marhc
"""
biggest = ()
def biggest_member(atuple):
    global biggest
    alist = [False if type(x) is tuple else True for x in atuple]
    if all(alist):
        return max(biggest, atuple)
    else:
        for i in atuple:
            print(i, "i")
            if type(i) is tuple:
                if len(i) > len(biggest):
                    biggest = i
                if len(biggest_member(i)) > len(biggest):
                    biggest = biggest_member(i)
        return biggest
        
print(biggest_member(((6, (10, 20, 5, 7), 8, 9, 10, 11), 5, (2, 3, 1))))