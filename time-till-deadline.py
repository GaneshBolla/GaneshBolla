import datetime

user_input = input("Enter your goal with deadline date speperated by colon :")
input_list = user_input.split(":")

goal = input_list[0]
dead_line = input_list[1]

dead_line = datetime.datetime.strptime(dead_line, '%d.%m.%Y')
today_date = datetime.datetime.today()
time_till = dead_line - today_date

print(f" Dead line date for your goal {goal}  is {time_till.days} days")

