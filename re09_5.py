# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:50:55 2019

@author: marhc
"""
import functools
def reduce_map_filter(args):
    if type(args) is list:
        return args
    if args[0] == "map":
        return list(map(args[1], reduce_map_filter(args[2])))
    if args[0] == "filter":
        return list(filter(args[1], reduce_map_filter(args[2])))
    if args[0] == "reduce":
        return functools.reduce(args[1], reduce_map_filter(args[2]))
print(reduce_map_filter(('reduce', lambda a,b: a+b, ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3])))	))