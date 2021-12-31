'''
contries = ['US','India','NewziLand','AUS','PAK',100,10.45,True,'SouthAfrica']
contries2 = list(('US','India','NewziLand','AUS','PAK',100,10.45,True,'SouthAfrica'))
print(type(contries))
print(type(contries2))
print(contries[2])
print(contries2)  # list can be decalre in two ways
print(contries[2][0])
print(contries[1:]) # print all values from Index 1 to nth index
print(contries[2:4])
print(contries[-1]) # last value from the list
print(contries[-2]) # last value from the list
contries[2] = 'Nokia'
print(contries[2])
print(len(contries))
'''


'''
user_input = ''
while user_input != "exit":
    user_input = input("Enter number of days i will convert into hours : ")
    validate_and_execute()
'''