# class attributes
"""class StarCookie:  
    pass
    
star_cookie1 = StarCookie()
print(star_cookie1)
# ther were the objects 
# now to write attributes of each objct
star_cookie1.weight = 15
star_cookie1.color = 'red'
print(star_cookie1.weight)
print(star_cookie1.color)
star_cookie2 = StarCookie()
star_cookie1.weight = 14
star_cookie1.color = 'orange'
print(star_cookie1.weight)
print(star_cookie1.color)"""

"""since the all objects in a class should have
a same attributses so in this case we can forgot or 
miswrite the attributes so to improve that """

# time wasting 
# second method

class StarCookie:
    milk = 0.1
    def __init__(self,color,weight):
        # initalize attributes 
        self.color = color
        self.weight = weight
star_cookie1 = StarCookie('red',32)
print(star_cookie1)
# ther were the objects 
# now to write attributes of each objct
print(star_cookie1.weight)
print(star_cookie1.milk)
print(star_cookie1.color)
print(star_cookie1.milk)
print(StarCookie.milk)

print(star_cookie1.__dict__)
# {'color': 'red', 'weight': 32}
print(StarCookie.__dict__)
"""{'__module__': '__main__', 'milk': 0.1, '__init__': <function StarCookie.__init__ at 0x7fd5202a39d0>, '__dict__': <attribute '__dict__' of 'StarCookie' objects>, '__weakref__': <attribute '__weakref__' of 'StarCookie' objects>, '__doc__': None}
Elshad"""

# star_cookie2 = StarCookie()
# star_cookie1.weight = 14
# star_cookie1.color = 'orange'
# print(star_cookie1.weight)

# can set default values 
class YouTube:
    def __init__(self, username, subscribers = 0):
        self.username = username
        self.subscribers = subscribers
        
user1 = YouTube('Elshad')
print(user1.username)
print(user1.subscribers)

user2 = YouTube('Renad')
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)

"""class attributes :->they act as global variables and is applicable for everything"""
