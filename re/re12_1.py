# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:49:59 2019

@author: marhc
"""
def collides(obj1, obj2):
    alist1 = [obj1[x] for x in obj1.keys()]
    alist2 = [obj2[y] for y in obj2.keys()]
    if alist1[3] < alist2[1] or alist1[1] > alist2[3] or alist1[0] > alist2[2] or alist1[2] < alist2[0]:
        return False
    else:
        return True

def number_of_collisions(objects):
    count = 0
    while len(objects) > 1:
        for i in range(1, len(objects)):
            if collides(objects[0], objects[i]):
                count += 1
        del objects[0]
    return count
print(number_of_collisions([{'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2}, {'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}]))