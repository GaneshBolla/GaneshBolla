def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        # return f"{num_of_days} days are {calc_to_units * num_of_days} {name_of_unit}"
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "un-supported unit"

    
def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_num = int(days_and_unit_dictionary["days"])
        if user_input_num > 0:
            calc_value = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(calc_value) 
        elif user_input_num == 0:
            print(" Please enter Valid +ve Number .... ")
        else:
            print("You are Entered -ve Number Please try again... ")
    except ValueError: 
        print(" Invalid Input value please provide valid input... ")

user_input_message = " Enter Number of Days, hours or minutes for Conversion : "