# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:01:07 2019

@author: marhc
"""

def isomorphic(astring1, astring2):
    map1 = {}
    string_not = "'" + astring1 + "' " + "and" + " '" + astring2 + "' " + "are not isomorphic" 
    string_yes = "'" + astring1 + "' " + "and" + " '" + astring2 + "' " + "are isomorphic because we can map: " + str(map1)
    for i in range(len(astring1) - 1):
        map1[astring1[i]] = astring2[i]
        if (astring1[i] in map1.keys() or astring2[i] in map1.values()) and map1[astring1[i]] != astring2[i]:
            return string_not
    return string_yes
print(isomorphic('ab', 'aa'))