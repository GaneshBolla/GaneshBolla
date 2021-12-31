'''try:
    num = int(input("Enter value : "))
    print(num)
except ValueError:
    print("Input value is not a Integer... Try again")
finally:
    print('Try & exception Block execution is completed and Finally block is active Now... ')'''


name_of_unit = "hours"
calc_to_units = 24

def days_to_units(num_of_days):
    return f"{num_of_days} days are {calc_to_units * num_of_days} {name_of_unit}"
    
def validate_and_execute():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            calc_value = days_to_units(user_input_num)
            print(calc_value) 
        elif user_input_num == 0:
            print(" Please enter Valid +ve Number .... ")
        else:
            print("You are Entered -ve Number Please try again... ")
    except ValueError: 
        print(" Invalid Input value please provide valid input... ")

user_input = input(" Enter a Value for days to hours conversion : ")
validate_and_execute()