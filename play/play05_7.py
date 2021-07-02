# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:04:30 2019

@author: marhc
"""

def remove_leading(ip):
    ip_list = ip.split(".")
    ip_list_1 = []
    for piece in ip_list:
        for i in piece:
            if piece[0] == "0" and piece != "0":
                piece = piece[1:]
        ip_list_1.append(piece)
    return (".".join(ip_list_1))

print(remove_leading('00.0.0000.0'))