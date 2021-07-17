'''
Daniel Wandeler
CS 4920
Homework 3 Programming problem 2

This program also uses the class AES and functions from aes.py from the following URL:
https://github.com/boppreh/aes
'''

import os, aes
import prettytable

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
