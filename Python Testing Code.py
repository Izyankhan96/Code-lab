print("Hello Please enter your name and password below to continue")
name = input("Name :")
while name != "Maxine":
   print("Invalid name Please re-enter your name")
   name = input("Name :")
print("Please enter your password below")
password = input("Password :")
while password != "Maxine_rocks":
   print("Invalid Password Please re-enter your password below")
   password = input("Password :")
print("Welcome back Maxine! You have successfully logged in")
print("Here are your grades for all 3 semesters")
grade_semester1 = 70
if grade_semester1 >= 95:
   print("A+")
elif grade_semester1 >= 90:
   print("A")
elif grade_semester1 >= 85:
   print("A-")
elif grade_semester1 >= 80:
   print("B+")
elif grade_semester1 >= 75:
   print("B")
elif grade_semester1 >= 70:
   print("B-")
elif grade_semester1 >= 65:
   print("C")
elif grade_semester1 >= 60:
   print("D")
else:
   print("F")
grade_semester2 = 89
if grade_semester2 >= 95:
   print("A+")
elif grade_semester2 >= 90:
   print("A")
elif grade_semester2 >= 85:
   print("A-")
elif grade_semester2 >= 80:
   print("B+")
elif grade_semester2 >= 75:
   print("B")
elif grade_semester2 >= 70:
   print("B-")
elif grade_semester2 >= 65:
   print("C")
elif grade_semester2 >= 60:
   print("D")
else:
   print("F")
grade_semester3 = 98
if grade_semester3 >= 95:
   print("A+")
elif grade_semester3 >= 90:
   print("A")
elif grade_semester3 >= 85:
   print("A-")
elif grade_semester3 >= 80:
   print("B+")
elif grade_semester3 >= 75:
   print("B")
elif grade_semester3 >= 70:
   print("B-")
elif grade_semester3 >= 65:
   print("C")
elif grade_semester3 >= 60:
   print("D")
else:
   print("F")
grade_good = True
passed = True
if grade_good and passed == True:
   print("You have passed with good grades")
else:
   print("You have Failed")