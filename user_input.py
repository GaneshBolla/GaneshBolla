#Global Variables
to_seconds = 24 * 60 * 60
to_min = 24 * 60
to_type_text = "minutes"
calc_to_units = 24
name_of_unit= "hours"

#Avoid duplications in above variables section Use Functions
#Functions  -- to avoid same repeating logic

def days_to_unit():
    print(f'In 35 days {35 * to_seconds} {to_type_text}')
    print("All Ok....")

def scope_check(name_of_unit):
    my_var="this is inside function variable"
    print(name_of_unit)
    print(my_var)

#Funtion with Arguments with local variables
def days_to_unit(num_of_days):
    if num_of_days > 0:
        return f'In {num_of_days} days {num_of_days * calc_to_units} {name_of_unit}'
    else:
        return "Entered value is Negative"

#my_var = days_to_unit(20)
#print(my_var)
user_input = input("Enter some values \n")
user_input_number = int(user_input)
caluclated_value = days_to_unit(user_input_number)
print(caluclated_value)