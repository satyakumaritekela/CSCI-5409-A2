'''
Created on Feb. 26, 2020

@author: satya
'''

import random as rand

numbers = []

# generating 100 random numbers
for i in range(100):
    n = rand.randint(1, 20)
    numbers.append(n)

# writing numbers into text file
with open('input.txt', 'w') as inputFile:
    for num in numbers:
        inputFile.write(str(num) + '\n')