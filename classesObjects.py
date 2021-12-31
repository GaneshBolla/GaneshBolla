#Class is a constructor of object
class my_class():
    x=5
p1 = my_class()
print(p1.x)


class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person('Ganesh', 40)
print(p1.name)
#del p1 # next step will not work since p1 object is deleted
print(p1.age)

# User Input values for class
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
name1 = input('Enter Name : ')
age1 = input('Enter Age : ')
p1 = person(name1,age1)
print(p1.name)
print(p1.age)

class members():
    pass # this will be empty class will not execute

class Student():
     name = 'Gane'
     age = 39
     Mobile = 7676867206
     gender = 'Male'