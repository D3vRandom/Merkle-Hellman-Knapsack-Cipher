#!/usr/bin/env python
# coding: utf-8

import random
import math
import os
import struct
'''
Author: Joshua Mol
Date: March, 6, 2020
Contact: joshua_mol@hotmail.ca
Version: 1
'''

def egcd(a, b):
    u = a
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    if (lastY < 0):
        lastY = u + lastY
    return (lastY)

def decrypt(encryptedMessage, u, v):
    inverseV = egcd(u, v)
    decryptedMessage = []
    for element in encryptedMessage:
        decryptedMessage.append(element * inverseV % u)
    return decryptedMessage

def subSetSum(array, target):
    res = {0 : []}
    for i in array:
        newres = dict(res)
        for v, l in res.items():
            if v+i < target:
                newres[v+i] = l+[i]
            elif v+i == target:
                return l+[i]
        res = newres
    return None

def binaryOrder(array, message):
    bindumpArray = []
    for text in message:
        subSet = []
        subSet = subSetSum(array, text)
        print("subSetSum of %d: \n%s" % (text, subSet))
        bindump = ""
        for x in range(0, len(array)):
            bindump = bindump + "0"
        #print(bindump)
        for element in subSet:
            bindump = bindump[:array.index(element)] + '1' + bindump[array.index(element)+1:]
        bindumpArray.append(bindump)
    return bindumpArray

A = {253442, 434472, 86178, 244768, 127476, 472188, 89198, 33572,30938, 242906, 377194, 218181, 291538, 53752, 252328, 432244}
encryptedMessage = {1685762, 2464793, 2117019, 1682388, 2588473, 2513425}
u = 500001
v = 36206
print("Question 1:  16-bit knapsack cipher has public key:\n")
decryptedA = decrypt(A, u, v)
decryptedA = sorted(decryptedA)
decryptedMessage = decrypt(encryptedMessage, u, v)
#decryptedMessage = sorted(decryptedMessage)
print("Reversed Trap Door Set: \n%s\n\nDecrypted Message Sums: \n%s\n" % (decryptedA, decryptedMessage))
binaryMessage = binaryOrder(decryptedA, decryptedMessage)
print("\n\nBinary Message   \"Answer Key?\":\n%s\n\n\n\n\n" % (binaryMessage))