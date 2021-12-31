from user import User
from post import Post

app_user_one = User("gb@gmail.com", "Ganesh", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

#app_user_one.change_jobTitile("Cloud Engineer")
#app_user_one.get_user_info()

app_user_two = User("james@gmail.com", "James Bond", "pwd1", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()