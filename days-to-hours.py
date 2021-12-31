name_of_unit = "hours"
calc_to_units = 24

# For Integer
def days_to_units(num_of_days):
    if num_of_days > 0 :
        return f"{num_of_days} days are {calc_to_units * num_of_days} {name_of_unit}"
    elif num_of_days == 0:
        return " Please enter Valid +ve Number .... "

    else:
        return "Entered value is Negative Number please try again.... "
'''
user_input = input(" Enter a Value for days to hours conversion : ")
user_input_num = int(user_input)

calc_value = days_to_units(user_input_num)
print(calc_value) '''

# handle user input is string or float

def validate_and_execute():
    if user_input.isdigit():
        user_input_num = int(user_input)
        calc_value = days_to_units(user_input_num)
        print(calc_value) 
    else: 
        print(" Invalid Input value please provide valid input... ")

user_input = input(" Enter a Value for days to hours conversion : ")
validate_and_execute()