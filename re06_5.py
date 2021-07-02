# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:19:59 2019

@author: marhc
"""
def anagram_test(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    list_s1 = list(string1)
    list_s2 = list(string2)
    list_s1 = [x for x in list_s1 if x != " "]
    list_s2 = [x for x in list_s2 if x != " "]
    result = True
    for i in list_s1:
        if i not in list_s2:
            result = False
    return result

#print(anagram_test('they see', 'the eyes'))
    
def anagrams(alist):
    f_list = []
    i = 0
    while i < len(alist):
        small_list = [alist[i]]
        n = 0
        while n < len(alist):
            print(alist[i], "i")
            print(alist[n], "n")
            if alist[i] != alist[n] and anagram_test(alist[i], alist[n]):
                small_list += [alist[n]]
                print(small_list)
            n += 1
        f_list.append(small_list)
        for word in small_list:
            alist.remove(word)
    return f_list
            

print(anagrams(['ferrari', 'Elon Musk', 'Muskmelon', 'rrarife', 'tenerife']))