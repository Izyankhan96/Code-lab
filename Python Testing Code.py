print("Hello user this is a place where you can add tasks, delete tasks and view them!")
print("Login")
name = input("Username :")
while name != "Izyan":
    print("Sorry Invalid username")
    name = input("Username :")
print("Welcome back Izyan!")
password = input("Password :")
while password != "123456789":
    print("Sorry Invalid Password")
    password = input("Password :")
print("Login Successful!")
print("Here are your tasks for today :")
tasks = ["Finish Book report", "Code a project", "Clean the house"]
for i in range(len(tasks)):
    print(i + 1, tasks[i])
option1 = input("Would you like to add something or delete something from your list? say yes to add, delete to delete a task and no to keep things as they are :")
if option1.lower() == "yes":
   new_task = input("Enter your new task :")
   tasks.append(new_task)
   print("Here are your updated tasks for today :")
for i in range(len(tasks)):
        print(i + 1, tasks[i])
if option1.lower() == "no":
    print("Alright no changes " \
    "made.")
if option1 == "delete":
     delete_task = input("Enter the task you want to delete :")
     tasks.remove(delete_task)
     print("Here are your updated tasks for today :")
for i in range(len(tasks)):
        print(i + 1, tasks[i])
        
    