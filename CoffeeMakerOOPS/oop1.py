class user:
    # pass  "this commmand is used when we just have to make our class or function empty"
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.user_name=user_name
        self.follower=0
        self.following=0

    def followers(self,user):
        user.follower+=1
        self.following+=1

user1=user("124","kritagyay")
print(user1.id)
print(user1.user_name)

user2=user("154","venom")
print(user2.id)
print(user2.user_name)

user1.followers(user2)
print(user1.follower)
print(user1.following)

print(user2.follower)
print(user2.following)