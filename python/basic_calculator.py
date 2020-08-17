'''
Ask the user their name
Have the user provide three numbers
Add the first number together, then multiply the results with the third number
Output the result in a long sentence that includes the user's name, the numbers they chose, and the following result
'''

name=input('Enter your name:')
print('Please enter the numbers you want to calculate:')
first=int(input('Enter first number:'))
second=int(input('Enter second number:'))
third=int(input('Enter third number:'))
sum=int((first+second)*third)
print('Your name is {} and your first number is {} and your second number is {} and your third number is {}. The result of the numbers is {}.'.format(name,first,second,third,sum))
