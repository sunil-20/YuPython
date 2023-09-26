# creating and using class / blueprint to create object
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


user_1 = User("001", "zombie")  # object
user_2 = User("002", "zack")

print(user_1.user_id)
print(user_1.username)

print(user_2.user_id)
print(user_2.username)