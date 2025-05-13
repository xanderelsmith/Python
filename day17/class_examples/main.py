from car import Car
from user import User

mercedes=Car(name='Mercedes')
print(mercedes.name)
user1=User("0012")
user1.assign_followers(10)
print(user1.followers)