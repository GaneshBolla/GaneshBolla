a = input('Enter Value for a : ')
b = input('Enter Value for b : ')
c = int(input('Enter integer value for c : '))
d = int(input('Enter integer value for d : '))


if a>b or a>=b:   # a == True or a == False
    print('a is lessthan b')
elif a == True:
    print('a is true')
elif c == a:
    print('value of a and c equal')
else:
    print('a is none of the above')


if type(c) == int:
    print(c, ' is a integer value')
else:
    print(c+ ' is not a integer value')

# Number divisible or not
e = c%d
if c%d == 0:
    print(c,' is divisable by ', d)
else:
    print(c, ' is Not divisable by ', d)
    print(' Next divisiable number is ', e+d)

# Even Number or Odd Number
if c%2 == 0:
    print(c, ' is Even Number')
else:
    print(c, " is ODD number")