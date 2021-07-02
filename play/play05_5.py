# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 00:26:15 2019

@author: marhc
"""
def repeated_letter(s):
    f_letter = ""
    s_list = list(s)
    stop = 0
    for letter in s_list:
        if stop == 1:
            break
        s_list_2 = s_list[0:s_list.index(letter)] + s_list[(s_list.index(letter)) + 1:]
        for letter_2 in s_list_2:
            if letter == letter_2:
                f_letter = letter
                stop = 1
                return f_letter
                break

print(repeated_letter('internet'))