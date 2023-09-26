# creating and using class / blueprint to create object
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0  # default value, no need to provide parameter in init.
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1


user_1 = User("001", "zombie")  # object
user_2 = User("002", "zack")

print(user_1.user_id)
print(user_1.username)

print(user_2.user_id)
print(user_2.username)

# call
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
