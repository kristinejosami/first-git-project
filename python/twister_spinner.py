'''
Create a program that emulates a twister spinner
Each time the program is run it outputs one of each of the following(at random):
-one colour(red.green,blue, yellow)
-one body part(left foot, right foot, left hand, right hand)
'''

print('This is a Twister Spinner Game!',
      "Let's Play!")
import random
colors=['red','green','blue','yellow']
body=['left foot', 'right foot', 'left hand', 'right hand']
colors_choice=random.choice(colors)
body_choice=random.choice(body)
print(colors_choice,'equals',body_choice)