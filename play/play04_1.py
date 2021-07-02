# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:39:11 2019

@author: marhc
"""
def validate(grade):
    while type(grade) is not int and type(grade) is not float:
        return False
        break
    while 0 <= grade <= 100:
        return True
        break
    while grade < 0 or grade > 100:
        return False
        break

print(validate(10.5))