def add_numbers(num1,num2):
    print('Hello Print message before return')
    return num1+num2
    print('Hello this message will not print after return statement')
    
num1 = int(input('Enter value for num1 : '))  # if int not added values of num1 & num2 will be concatenated.
num2 = int(input('Enter val10ue for num2 : '))
print(add_numbers(num1,num2))   