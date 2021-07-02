# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:45:54 2019

@author: marhc
"""

def manipulator(l, cmds):
    result_list = ""
    for i in cmds:
        if i[0:6] == "insert":
            l.insert(int(i[7]), int(i[9:]))
        if i == "print":
            if len(result_list) > 0:
                result_list += " " + str(l)
            else:
                result_list += str(l)
        if i[0:6] == "remove":
            l.remove(int(i[7]))
        if i[0:6] == "append":
            l.append(int(i[7:]))
        if i == "sort":
            l.sort()
        if i == "pop":
            l.pop()
        if i == "reverse":
            l.reverse()
    return result_list

print(manipulator([], ['append 1', 'append 3', 'pop', 'append -1', 'print']))