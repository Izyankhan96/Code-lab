print("Welcome to my Task Manager!")
login = input("Please enter your username :")
username = "Izi"
while login != username:
    print("Invalid Username, Please try again.")
    login = input("Please enter your username :")
print("Welcome back, Izi!")
password = input("Please enter your password :")
user_password = "1234"
while password != user_password:
    print("Invalid Password, Please try again.")
    password = input("Please enter your password :")
print("You have successfully logged in!")
tasks = ["Clean the house", "Do the laundry", "Finish the report","Pratice Python"]
print("Your tasks for today :")
for i in range(len(tasks)):
    print(i + 1, tasks[i])
print("if you would like to add or change a task please select from the following options below :")
options = ["Add","Delete","None"]
for i in range(len(options)):
    print(i + 1, options[i])
options_choice = input("Please select an option : ")
if options_choice == "Add":
    new_task = input("Please enter the new task you would like to add :")
    tasks.append(new_task)
    print("Your updated tasks for today are :")
    for i in range(len(tasks)):
        print(i + 1, tasks[i])
if options_choice == "Delete":
    delete_task = input("Please enter the task number you would like to delete :")
    tasks.remove(delete_task)
    print("Your updated tasks for today are :")
    for i in range(len(tasks)):
            print(i + 1, tasks[i])
    
if options_choice == "None":
    print("No changes made to your tasks.")
    for i in range(len(tasks)):
        print(i +1, tasks[i])