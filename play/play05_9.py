# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:48:46 2019

@author: marhc
"""

def summary_ranges(astring):
    astring_list = astring.split(",")
    print(astring_list)
    final_string = astring[0]
    for i in astring_list[1:]:
        if astring_list.index(i) + 1 != len(astring_list):
            if int(i) + 1 != int(astring_list[astring_list.index(i)]) and int(i) - 1 != int(astring_list[astring_list.index(i) - 1]):
                final_string += "," + i
            elif int(i) + 1 != int(astring_list[astring_list.index(i) + 1]) and int(i) - 1 == int(astring_list[astring_list.index(i) - 1]):
                final_string += "->" + i
        else:
            if int(i) - 1 != int(astring_list[astring_list.index(i) - 1]):
                final_string += "," + i
            elif int(i) - 1 == int(astring_list[astring_list.index(i) - 1]):
                final_string += "->" + i
    return final_string
            
            
print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))