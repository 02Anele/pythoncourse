'''
Created on 08 Nov 2016

@author: mark
'''
from random import randint

min_rnd = int(raw_input("Enter the min random "))
max_rnd = int(raw_input("Enter the max random "))

rnd = randint(min_rnd,max_rnd)

print rnd
#guess = -1
#while guess !=rnd:
for x in range(5):
    guess = int(raw_input("Enter your guess "))
    if guess > rnd: print "too high"
    elif guess < rnd: print "too low"
    else: 
        print "correct"
        break
else: print "you lose"