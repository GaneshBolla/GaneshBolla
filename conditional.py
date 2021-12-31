
calc_to_units = 24
name_of_unit= "hours"

def days_to_unit(num_of_days):
    if num_of_days > 0:
        print(type(num_of_days))
        return f'In {num_of_days} days {num_of_days * calc_to_units} {name_of_unit}'
    else:
        return "Entered value is Negative"

#my_var = days_to_unit(20)
#print(my_var)
user_input = input("Enter some values \n")
user_input_number = int(user_input)
caluclated_value = days_to_unit(user_input_number)
print(type(caluclated_value))
print(caluclated_value)
