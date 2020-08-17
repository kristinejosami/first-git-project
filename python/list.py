'''
Create a list
Add a list in this list
Add a list within this list
Each list must contain at least four elements

Access the first two elements of the list within the original list
Access the last three elements of the list within the list within the list
Output the whole thing backwards
'''

first_list=[1,2,3,[4,5,6,[7,8,9,10]]]
a=first_list
print(first_list[3][:2])
print(first_list[3][3][1:])
print(a[::-1])