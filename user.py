# Class is a blue print for specific object
# in blue print we don't have specific values only attributes declare

class User:
    def __init__(self,email,name,password,job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_jobTitile(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"{self.name} currently works as a {self.job_title}. You can contact him at {self.email}")

# Moving below code to main-user.py file
'''app_user_one = User("gb@gmail.com", "Ganesh", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_jobTitile("Cloud Engineer")
app_user_one.get_user_info()'''