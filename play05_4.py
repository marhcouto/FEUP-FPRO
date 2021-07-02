# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:28:05 2019

@author: marhc
"""

def map1(pos, steps):
    steps_list = steps.split("-")
    x = pos[0]
    y = pos[1]
    for step in steps_list:
        if step == "right":
            x += 1
        if step == "left":
            x -= 1
        if step == "up":
            y += 1
        if step == "down":
            y -= 1
    return (x, y)