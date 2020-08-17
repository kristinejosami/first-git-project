'''
Create a game where:
User has to do something against the computer
Have a condition where the user can lose lives based on their guess
User has five lives per game
When they run out of lives the game ends and they get a 'Game Over' message
'''
print('This is a letter guessing challenge')
from random import randint
#number=int(randint(1,10))
#print(number)
user_lives=5
while 1==1:
    number = int(randint(1, 10))
    #print(number)
    guess=int(input('Enter guess: '))
    if guess==number:
        print('You win!!!')
    else:
        print('You lose. You lose a life.')
        user_lives-=1
        print('Lives left: {}'.format(user_lives))

    if user_lives==0:
        break


#print('GAME OVER!!! Your guess was {} and the computer was {}.'.format(guess,number))