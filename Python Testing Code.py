print("Hello Welcome Please Login below")
name = input("Name :")
verified_name = "Izyan"
while name != verified_name:
    print("Sorry I dont see your name Please try again")
    name = input("Name :")
print("Please Enter your password below")
password = input("Password :")
verified_password = "Welcome7643"
while password != verified_password:
    print("Incorrect Password")
    password = input("Password :")
print("Welcome![before we continue you have to guess the correct questions]")
import random
colors = ["Red","Blue","Green"]
for i in range(len(colors)):
    print(i + 1, colors[i])
result = random.choice(colors)
answer = input("Enter your answer here :")
while answer != random.choice:
    print("Sorry That is incorrect please try again")
    answer = input("Enter your answer here :")
print("That is correct!")
print(result)