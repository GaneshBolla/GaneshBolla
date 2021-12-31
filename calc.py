#num1 = input("Enter First Number: ")
#num2 = input("Enter Second Number: ")  # this is concatinating the num1 & num2 as its considoring as string
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
op = input("Enter Operator for Numbers: ")

print(num1%num2)
if op == '+':
    print("Sum of num1 and num2 is", num1+num2) 
elif op == '*':
    print('Multiply of num1 and num2 is ', num1*num2)
elif op == '-':
    print('Subtraction of num1 & num2 is ', num1-num2)
elif op == '/':
    print('Division of num1 & num2 is ', num1/num2)
elif op == '%':
    print('Reminder of num1 & num2 is ', num1%num2)
else:
    print("Invalid Operator")