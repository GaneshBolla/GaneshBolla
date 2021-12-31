name_of_unit = "hours"
calc_to_units = 24

def days_to_units(num_of_days):
    return f"{num_of_days} days are {calc_to_units * num_of_days} {name_of_unit}"
    
def validate_and_execute():
    try:
        user_input_num = int(num_of_days_element)
        if user_input_num > 0:
            calc_value = days_to_units(user_input_num)
            print(calc_value) 
        elif user_input_num == 0:
            print(" Please enter Valid +ve Number .... ")
        else:
            print("You are Entered -ve Number Please try again... ")
    except ValueError: 
        print(" Invalid Input value please provide valid input... ")


#while True:  # No more exit for loop
user_input = ""
while user_input != "exit": # if input is exit loop will break
    user_input = input(" Enter a Value for days to hours conversion : ")
    list_of_days = user_input.split(",")
    
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    for num_of_days_element in set(list_of_days):
        validate_and_execute()