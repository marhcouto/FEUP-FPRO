# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:42:07 2019

@author: marhc
"""

def file_finder(dirs, file_name):
    if file_name == dirs[0]:
        return file_name
    if file_name in dirs[1:]:
        return dirs[0] + "/" + file_name
    else:
        return dirs[0] + "/" + file_finder(dirs[1], file_name)
    
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], '22'))