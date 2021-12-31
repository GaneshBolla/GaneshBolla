#Global Variables
to_seconds = 24 * 60 * 60
to_min = 24 * 60
to_type_text = "minutes"
name_of_unit= "hours"

#Avoid duplications in above variables section Use Functions
#Functions  -- to avoid same repeating logic

def days_to_unit():
    print(f'In 35 days {35 * to_seconds} {to_type_text}')
    print("All Ok....")

days_to_unit()

#Funtion with Arguments with local variables

def days_to_unit(num_of_days):
    print(f'In {num_of_days} days {num_of_days * to_seconds} {to_type_text}')
    print("All Ok for num of days argument....")

# calling Funtion with arguments
days_to_unit(21)
days_to_unit(22)
days_to_unit(30)

def scope_check(name_of_unit):
    my_var="this is inside function variable"
    print(name_of_unit)
    print(my_var)

scope_check(20)

# Function with Arguments
def greetings_fun(name,age):
    print('Wel-come '+name+ ' You are '+str(age)+' Years old' )

greetings_fun('john',37)

# Multiple values as arguments and print the one with index
def greetings_fun(*names):
    print('Wel-come '+names[2])

greetings_fun('john', 'tim', 'tom')

#input values by user and output the same
def greetings_fun(name,age):
    print('Wel-come '+name+ ' You are '+str(age)+' Years old' )

name = input('Enter name : ')
age = input('Enger age : ')
greetings_fun(name, age)