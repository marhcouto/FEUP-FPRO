# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:56:27 2019

@author: marhc
"""
import math 

def tfidf(documents):
    the_list = []
    the_list2 = []
    for i in documents:
        sentence = (i.lower()).split()
        the_list += sentence
        the_list2.append(sentence)
    the_dick = {x:[0.0 for y in range(len(documents))] for x in the_list}
    N = len(the_list2)
    for word in the_dick:
        n = 0
        for i in range(N):
            if word in the_list2[i]:
                n += 1
                for another_word in the_list2[i]:
                    if word == another_word:
                        (the_dick[word])[i] += 1
        for i in range(N):
            the_dick[word][i] = round(the_dick[word][i] * math.log(N / n), 3)
    return the_dick
    
print(tfidf(['To be or not to be', 'Impossible is a word to be found only in the dictionary of fools', 'There is nothing impossible to him who will try']))