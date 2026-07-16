name = input("What is your name? :")
while name != "John":
   print("Invalid name please try again")
   name = input("What is your name? :")
print("Please enter your password below:")
password = input("What is your password? :")
while password != "125437":
   print("Invalid password please try again")
   password = input("What is your password? :")
print("Please verify your age below by taking a picture")
verification = input("Please take a picture below if you have done it please write done :")
while verification != "done":
   print("Invalid verification please try again")
   verification = input("Please take a picture below if you have done it please write done :")
print("Alright you will find out down below if you have made it in or not")
grade = 60
if grade >= 95:
   print("A+")
elif grade >= 90:
   print("A")
elif grade >= 80:
   print("B")
elif grade >= 70:
   print("C")
elif grade >= 60:
   print("D")
else:
   print("F")
fail = 60
did_not_make_it = False
if fail and did_not_make_it == False:
   print("Unfortunatly you did not make it in")
else:
   print("Congratulations you made it in")
