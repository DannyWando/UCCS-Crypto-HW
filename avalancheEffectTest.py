'''
Daniel Wandeler
CS 4920
Homework 3 Programming problem 3

This program is an extension of using AES in a computer to study the Avalanche Effect.
It also creates a formatted table of the output, entry values, and plaintext.

Uses aes.py and prettytable that are imported in cryptoHW3_pp2.py
'''

import os, aes, prettytable

def keyExpansion(startKey):
    return startKey
    # do stuff


print('Program starting...')
plaintext = "0321456789abcdeffedcba9876543210"
startKey = "0f0071c947d9e8591cb7add6af7f6798"
iv = os.urandom(16)

print('The start key is: ', startKey)
print('The plaintext is: ', plaintext)

ciphertext = aes.encrypt(startKey, plaintext)

print(ciphertext)
print('Program completed...')