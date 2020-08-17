'''
Create a program that:
Chooses a number between 1 to 100
Takes a users guess and tells them if they are correct or not

Bonus: Tell the user if their guess was lower or higher than the computer's number
'''


print('Number Guessing Challenge')
guess=int(input('This is a number guessing Challenge. Please enter your guess number:'))
from random import randint
number=int(randint(1,100))
# number=3
if number==guess:
    print('Congratulations! Your guess is correct. The number is {} and your guess is {}.'.format(number, guess))
elif number<guess:
    print("Sorry, your number is incorrect. The number is {} and your guess is {}."
          " Your guess is greater than the number. Please try again.".format(number,guess))
else:
    print("Sorry, your number is incorrect. The number is {} and your guess is {}. "
          "Your guess is lesser than the number. Please try again.".format(number, guess))
