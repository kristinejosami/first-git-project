'''
Create the same guessing game as before (computer randomly generates a number, user has to guess)
Make it so that the user only has to run the programme once, and keep guessing until they get it right
'''
print('This is a Number Guessing Challenge!!!')
from random import randint
number=int(randint(1,100))
#print(number)
while 'play'=='play':
    guess=int(input('Enter your guess: '))
    if guess==number:
        print('You win!!!')
        break
    elif guess>number:
        print('Too high')
    else:
        print('Too low')

print('Your guess was {} and computer was {}.'.format(guess,number))