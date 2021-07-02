# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:54:15 2019

@author: marhc
"""
def value(direc):
    if direc == "UP":
        return 1
    if direc == "DOWN":
        return -1
    if direc == "RIGHT":
        return 2
    if direc == "LEFT":
        return -2
def test(path):
    stop = False
    for i in range(len(path) - 1):
        if value(path[i]) + value(path[i + 1]) == 0:
            stop = True
    return stop

def min_path(path):
    i = 0
    while test(path):
        i = 0
        while i < len(path) - 1:
            direc = path[i]
            direc2 = path[i + 1]
            print(direc, "direc")
            print(direc2, "direc2")
            if value(direc) + value(direc2) == 0:
                del path[i]
                del path[i]
                print(path)
                print(test(path))
                break
            else:
                i += 1
            print(path, "path")
    return path

print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))