# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:36:44 2019

@author: marhc
"""

def binary_tree(key, tree):
    while True:
        if key == tree[0]:
            return tree[1]
        elif key > tree[0]:
            tree = tree[3]()
        elif key < tree[0]:
            tree = tree[2]()
print(binary_tree('hummer', ('aptitudes', 495, lambda: 1/0, lambda: ('roadblock', 25, lambda: ('paramedic', 211, lambda: ('bizets', 115, lambda: 1/0, lambda: ('modernizes', 848, lambda: ('lees', 937, lambda: ('gusty', 472, lambda: 1/0, lambda: ('haggles', 648, lambda: 1/0, lambda: ('jaclyns', 170, lambda: ('implication', 297, lambda: ('hummer', 561, lambda: 1/0, lambda: 1/0), lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))