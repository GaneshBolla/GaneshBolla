#name_of_unit = "hours"
#calc_to_units = 24

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        # return f"{num_of_days} days are {calc_to_units * num_of_days} {name_of_unit}"
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "un-supported unit"

    
def validate_and_execute():
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


#while True:  # No more exit for loop
user_input = ""
while user_input != "exit": # if input is exit loop will break
    user_input = input(" Enter Number of Days and Conversion : ")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

    validate_and_execute()

    '''
message = "Enter some value"
days = 20
price = 9.9
valid_number = True
exit_input = False
list_of_days = [10,20,30,40]
list_of_months = ["January","Feb","march","Apri"]
set_of_days = {10,20,30}
days_to_unit = {"days":10, "unit":hours }

    '''