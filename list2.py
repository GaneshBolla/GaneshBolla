list1 = [100, 5, 12, 208, 65, 3]
list2 = ['a','b','banana','ele','apple']

list1.sort()
print('Assending order of List1 is: ', list1)

list1.append(list2)
print('values of List1 : ',list1)
list2.append('cherries')
print('appended sting to list2 : ',list2)

print('Length of the list2 is : ',len(list2))

list2.insert(2,'Mango') # add the value to the list at specific position
print('Insert string to list2 at runtime : ',list2)
list2.remove('a')
print('remove string from list : ',list2) # remove strings from list and print

list3 = list2.reverse()
print('Reverse of the List2', list3)

list3 = list2.pop()
list3 = list2.remove()
del list2[0] # delete the index 0 from List2
del list2 # delete the list
