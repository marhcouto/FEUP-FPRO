# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:11:04 2019

@author: marhc
"""

def map1(pos, steps):
    if len(steps) == 0:
        return pos
    elif steps[0] == "up":
        del steps[0]
        return map1((pos[0], pos[1] + 1), steps)
    elif steps[0] == "down":
        del steps[0]
        return map1((pos[0], pos[1] - 1), steps)
    elif steps[0] == "right":
        del steps[0]
        return map1((pos[0] + 1, pos[1]), steps)
    elif steps[0] == "left":
        del steps[0]
        return map1((pos[0] - 1, pos[1]), steps)
print(map1((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))