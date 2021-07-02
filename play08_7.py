# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:46:52 2019

@author: marhc
"""
def checker(string):
    if len(string) == 1:
        return True
    if string[0] == "1" and string[1] == "1":
        return False
    else:
        return checker(string[1:])

def binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary(n // 2) + str(n % 2)
def zero_adder(str_n, zeros):
    if zeros == 0:
        return str_n
    else:
        return zero_adder("0" + str_n, zeros - 1)
    
def digiter(str_n, digits):
    if len(str_n) == digits:
        return str_n
    else:
        zeros = digits - len(str_n)
        return zero_adder(str_n, zeros)
    
def the_number_maker(integer, digits):
    return (digiter(binary(integer), digits))


def the_list_maker(n):
    alist = []
    def making(n1):
        if n1 == 0:
            alist.append(the_number_maker(0, n))
        else:
            alist.append(the_number_maker(n1, n))
            return making(n1 - 1)
    making(2**(n) - 1)
    return alist

def no_consecutives1(k):
    def _2_(alist, count):
        if len(alist) == 0:
            return count
        else:
            if checker(alist[0]):
                return _2_(alist[1:], count + 1)
            else:
                return _2_(alist[1:], count)
    return _2_(the_list_maker(k), 0)