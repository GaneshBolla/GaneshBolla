#while True:  # No more exit for loop

#import helper # to import all functions from helper.py 
#from helper import validate_and_execute, user_input_message 
# # to import specific function,variable from helper.py in this case function name ref not required for function. like below
# helper.validate_and_execute(days_and_unit_dictionary)

from helper import * 
# this willimport all
import logging

user_input = ""
while user_input != "exit":
    # if input is exit loop will break
    #user_input = input(" Enter Number of Days and Conversion : ")
    user_input = input(user_input_message) #user Input variable
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

    #helper.validate_and_execute(days_and_unit_dictionary) # this is not required if we import helper.py file
    validate_and_execute(days_and_unit_dictionary)


logger = logging.getlogger("MAIN")
logger.error("Error in the application")