print('Create your Account... ')
username = input('Enter Username : ')
password = input('Enter Password : ')

print('Your Account has been created successfully.. \n Login Now..')

username2 = input('Enter UserName : ')
password2 = input('Enter Password : ')

if username == username2 and password == password2:
    print('Login Successfull..')
else:
    print('Invalid credentials')

