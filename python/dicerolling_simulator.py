'''
Create a program that simulates two dice being rolled
In the program give a message to the user saying what the two dice values are and their combined total
'''
print('THIS IS A Simulation of Two Dice Rolling')
from random import randint
dice_one= randint(1,6)
dice_two= randint(1,6)
sum=dice_one+dice_two
print('Dice one value is {} and Dice two value is {}. Their combined total is {}.'.format(dice_one,dice_two,sum))