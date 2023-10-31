# Class methods-> behavior of ibject
#   function in a class is a method 
# object.funciton_name()

class YouTube:
    def __init__(self, username, subscribers = 0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    def subscribe(self, user):
        user.subscribers +=1 
        self.subscriptions += 1
        
user1 = YouTube('Elshad')
user2 = YouTube('Renad')
user1.subscribe(user2)
print(f"user 1 subscribers:{user1.subscribers}")
print(f"user 1 subscribcriptions:{user1.subscriptions}")
print(f"user 2 subscribers:{user2.subscribers}")
print(f"user 2 subscribscription:{user2.subscriptions}")


