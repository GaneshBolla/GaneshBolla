# for loop for iterating over sequence
# Example 1:
for letter in "Hlo":
    print(letter)

# Example 2:
my_list = ['hi','chinu','happy']
for value in my_list:
    print(value)

# Example 3:
my_dic = {
    'name': 'Ganesh',
     'age': '38'
}
for x in my_dic:
    print(x)

# Example 4: break for loop when match found
my_list = ['hi','ji','pr','mg']
for value in my_list:
    print(value)
    if value == 'pr':
        break

for x in range(3,8):
    print(x)
else:
    print('Finished looping')