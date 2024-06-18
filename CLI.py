# This file contains programs for Day 1 through 15 from the Python Mega Course
# to build 20 applications
# ToDo CLI (Command Line Interface) is the first application

# from module.functions import get_todos, write_todos, show_todo
# import module.functions as functions
# from dis import Instruction
from module import functions
import time
# import json


#Day 15
# Use of JSON file

# quiz_questions = [{'questions_text':'What are Dolphins', 
#                    'alternatives': ["Amphibians", "Fish", "Mammals", "Birds"], 
#                    'correct_answer': 3}, 
#                   {'questions_text': "What occupies most of the Earth's surface",
#                     'alternatives': ["Land", "Water"], 
#                     'correct_answer': 2}]

# with open("quiz_questions.json", 'r') as myfile:
#     content = myfile.read()

# #print(type(content))

# quiz_data = json.loads(content)
# # print(type(quiz_data))
# # print(quiz_data)

# for question in quiz_data:
#     print(question["question_text"])
#     for index, alternative in enumerate(question["alternatives"]):
#         print(index+1, "-", alternative)
#     user_choice = int(input("Enter your answer: "))    
#     question["user_choice"] = user_choice
    
# score = 0
# for index, question in enumerate(quiz_data):
#     if question["user_choice"] == question["correct_answer"]:
#         score = score + 1
#         result = "Correct answer "
#         #print("Your Score is: ", score, "/", len(quiz_data))
#     else:
#         result = "Wrong answer "
#         #print("Your Score is: ", score, "/", len(quiz_data))
#     message = f"{index+1} - {result} Your answer: {question['user_choice']}, " \
#               f"Correct answer: {question['correct_answer']}"  
#     print(message)

# print(score, '/', len(quiz_data))


#Day 14

# Main program begins here    

current_time = time.strftime("%A, %b %d, %Y - %H:%M:%S")
print("Today is ", current_time)

functions.user_guidelines()   # how to use the ToDo program

# Get already existing list of todos and display
todos = functions.get_todos()
functions.show_todo(todos)    

# Add / Edit / Remove todo items
while True:
    try:
        user_action = input("Type add, edit, completed or exit: ")
        user_action = user_action.strip()

        if user_action.startswith('add'):
            if user_action[4:]:
                todo = user_action[4:] + '\n'
                todos = functions.get_todos()
                todos.append(todo)
                functions.write_todos(todos)
                todos = functions.get_todos()
                functions.show_todo(todos)
            else:
                print("Enter a todo item")

        elif user_action.startswith('edit'):
            if user_action[5:].isdigit():
                number = int(user_action[5:])
                new_todo = input("Enter new ToDo item: ") + '\n'
                todos[number-1] = new_todo
                functions.write_todos(todos)
                todos = functions.get_todos()
                functions.show_todo(todos)
            else:
                print("ENTER the serial number of the todo to be edited")
            
        elif user_action.startswith('completed'):
            try:
                number = int(user_action[10:])
                completed_todo = todos[number-1].rstrip('\n')
                todos.remove(todos[number - 1])
                print(f"Item -{completed_todo}- is removed")
                functions.write_todos(todos)
                todos = functions.get_todos()
                functions.show_todo(todos)
            except IndexError:
                print("There are fewer items in the list, Please check and enter again")
                continue
            except ValueError:
                print("ENTER the serial number of the todo item to be removed")
                continue

        elif user_action.startswith('exit'):
            break
        
        else:
            print("Type add, edit, completed or exit ONLY: ")
    
    except KeyboardInterrupt:
        print("Please add todo items to create todos.txt file")
        print("Exiting the program as todo list is empty... ")
        break

print("Thank you & Bye!")

#Day 13
# about doc-string also called multiline string

# def parser(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return {'feet':feet, 'inches':inches}

# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * .0254
#     return meters

# height = input("Enter height in feet inches: ")

# parsed = parser(height) 
# print(parsed)
# result = convert(parsed['feet'], parsed['inches'])

# print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

# if result < 1:
#     print("Kid is too young for a roller coaster ride")
# else:
#     print("Kid is grown enough to ride the slide")    

# text = """Principles of productivity:
# Managing your inflows
# Systemizing everything that repeats."""

# print(text)

# Day 11 & 12

# Function to get the todo list from file
# def get_todos():
#     """function to get the todo list from file""" 
#     with open('todos.txt', 'r') as myfile_local:
#        todos_local = myfile_local.readlines()
#     return todos_local

# # Function to write the todo list into a file
# def write_todos(todos_local):
#     with open('todos.txt', 'w') as myfile_local:
#         myfile_local.writelines(todos_local)
#     return 0

# # Function to display the todo list
# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             item = item.rstrip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# # Instructions to use program
# def instructions():
#     print("Instruction for using todo Command Line Program")
#     print("1. To add a todo item type <add watch movie>")
#     print("2. To edit a todo item type <edit 5 i.e. todo item's serial number>")
#     print("3. To remove a todo item type <completed 5 i.e. completed todo item's serial number>")
#     print("4. To exit program type <exit>")
#     return 0

# Main program begins here    
# print(help(get_todos))
# while True:
#     todos = get_todos()
#     show_todo(todos)
#     instructions()
#     user_action = input("Type add, edit, completed or exit: ")
#     user_action = user_action.strip()

#     if user_action.startswith('add'):
#         todo = user_action[4:] + '\n'
#         todos = get_todos()
#         todos.append(todo)
#         write_todos(todos)

#     elif user_action.startswith('edit'):
#         if user_action[5:].isdigit():
#             number = int(user_action[5:])
#             new_todo = input("Enter new ToDo item: ") + '\n'
#             todos[number-1] = new_todo
#             write_todos(todos)
#         else:
#             print("ENTER the serial number of the todo to be edited\n")
        
#     elif user_action.startswith('completed'):
#         try:
#             number = int(user_action[9:])
#             completed_todo = todos[number-1].rstrip('\n')
#             todos.remove(todos[number - 1])
#             print(f"Item -{completed_todo}- is removed")
#             write_todos(todos)
#         except IndexError:
#             print("There are fewer items in the list, Please check and enter again")
#             continue
#         except ValueError:
#             print("ENTER the serial number of the todo item to be removed")
#             continue

#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Enter add, completed, exit only: ")

# print("Bye!")


# #Day 10

# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             item = item.rstrip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# #todos = []

# while True:
    
#     with open('todos.txt', 'r') as myfile:
#             todos = myfile.readlines()
#             show_todo(todos)
    
#     user_action = input("Type add, edit, completed or exit: ")
#     user_action = user_action.strip()

#     if user_action.startswith('add'):
#         todo = user_action[4:] + '\n'
                
#         with open('todos.txt', 'r') as myfile:
#             todos = myfile.readlines()

#         todos.append(todo)
        
#         with open('todos.txt', 'w') as myfile:
#             myfile.writelines(todos)

# #    elif 'show' in user_action:
# #                
# #        with open('todos.txt', 'r') as myfile:
# #            todos = myfile.readlines()
# #
# #        show_todo(todos)

#     elif user_action.startswith('edit'):
        
#         if user_action[5:].isdigit():
#             number = int(user_action[5:])
#             new_todo = input("Enter new ToDo item: ") + '\n'
#             todos[number-1] = new_todo

#             with open('todos.txt', 'w') as myfile:
#                 myfile.writelines(todos)
#         else:
#             print("ENTER the serial number of the todo to be edited\n")
        
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             completed_todo = todos[number-1]
#             todos.remove(todos[number - 1])
            
#             print(f"Item {completed_todo.strip('/n')} is removed")

#             with open('todos.txt', 'w') as myfile:
#                 myfile.writelines(todos)
#         except IndexError:
#             print("There are fewer items in the list, Please check and enter again")
#             continue
        
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Enter add, show, exit only: ")

# print("Bye!")

# #Day 9

# #check strength of the password
# #password should meet three coonditions to be strong
# #password should be minimum 8 chars lenght, should include one numeric value
# #password should have atleast one upper character

# user_password = input("Enter password: ")
# password_lenght = len(user_password)
    
# result = {"length":False, "upper":False, "digit":False}
# #print(result)

# if password_lenght >= 8:
#     result["length"] = True

# for char in user_password:
#     if char.isupper():
#         result["upper"] = True
#         break

# for num in user_password:
#     if num.isdigit():
#         result["digit"] = True
#         break

# if all(result.values()):
#     print("Password is strong")
# else:
#     print("Password is week")

# if result["length"] == False:
#     print("password should be of minimum 8 characters")
# elif result["upper"] == False:
#     print("Password should contain at least one uppercase character")
# elif result["digit"] == False:
#     print("Password should contain at least one digit")        

# #function to show the todo list
# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             item = item.rstrip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# #todos = []

# while True:
    
#     with open('todos.txt', 'r') as myfile:
#             todos = myfile.readlines()
#             show_todo(todos)
    
#     user_action = input("Type add, edit, completed or exit: ")
#     user_action = user_action.strip()

#     if 'add' in user_action:
#         todo = user_action[4:] + '\n'
                
#         with open('todos.txt', 'r') as myfile:
#             todos = myfile.readlines()

#         todos.append(todo)
        
#         with open('todos.txt', 'w') as myfile:
#             myfile.writelines(todos)

# #    elif 'show' in user_action:
# #                
# #        with open('todos.txt', 'r') as myfile:
# #            todos = myfile.readlines()
# #
# #        show_todo(todos)

#     elif 'edit' in user_action:
        
#         number = int(user_action[5:])
#         new_todo = input("Enter new ToDo item: ") + '\n'
#         todos[number-1] = new_todo

#         with open('todos.txt', 'w') as myfile:
#             myfile.writelines(todos)

#     elif 'complete' in user_action:
        
#         number = int(user_action[9:])
#         completed_todo = todos[number-1]
#         todos.remove(todos[number - 1])
        
#         print(f"Item {completed_todo.strip('/n')} is removed")

#         with open('todos.txt', 'w') as myfile:
#             myfile.writelines(todos)

#     elif 'exit'in user_action:
#         break
#     else:
#         print("Enter add, show, exit only: ")

# print("Bye!")

# #Day 8

# with open(".\\file_access\\name_list.txt", 'r') as myfile:
#     print(myfile.read())


# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             item = item.rstrip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# #todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("\nEnter a todo: ") + "\n"
            
#             with open('todos.txt', 'r') as myfile:
#                 todos = myfile.readlines()

#             todos.append(todo)
            
#             with open('todos.txt', 'w') as myfile:
#                 myfile.writelines(todos)

#         case 'show' | 'display':
            
#             with open('todos.txt', 'r') as myfile:
#                 todos = myfile.readlines()

#             show_todo(todos)

#         case 'edit':
#             with open('todos.txt', 'r') as myfile:
#                 todos = myfile.readlines()
            
#             show_todo(todos)
            
#             number = int(input("Type serial number of ToDo to be edited: "))
#             new_todo = input("Enter new ToDo item: ") + '\n'
#             todos[number-1] = new_todo

#             with open('todos.txt', 'w') as myfile:
#                 myfile.writelines(todos)

#         case 'complete' :
#             with open('todos.txt', 'r') as myfile:
#                 todos = myfile.readlines()
            
#             show_todo(todos)
            
#             number = int(input("Type serial number of ToDo completed: "))
#             todos.remove(todos[number - 1])
            
#             with open('todos.txt', 'w') as myfile:
#                 myfile.writelines(todos)

#         case 'exit':
#             break
#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")

# # #Day 7

# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             item = item.rstrip('\n')
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# #todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("\nEnter a todo: ") + "\n"
            
#             file = open("todos.txt", "r")
#             todos = file.readlines()
#             file.close()

#             todos.append(todo)
            
#             file = open("todos.txt", "w")
#             todos = file.writelines(todos)
#             file.close()

#         case 'show' | 'display':
#             file = open("todos.txt", 'r')
#             todos = file.readlines()
#             file.close()
            
#             #new_todos = []
#             #for item in todos:
#             #    new_item = item.strip('\n')
#             #    new_todos.append(new_item)

#             #new_todos = [item.strip('\n') for item in todos]
#             show_todo(todos)

#         case 'edit':
#             show_todo(todos)
#             number = int(input("Type serial number of ToDo to be edited: "))
#             new_todo = input("Enter new ToDo item: ")
#             todos[number-1] = new_todo 
#         case 'complete' :
#             show_todo(todos)
#             number = int(input("Type serial number of ToDo completed: "))
#             todos.remove(todos[number - 1])
#         case 'exit':
#             break
#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")

# #Day 6
# filenames = ['a.txt', 'b.txt', 'c.txt']

# for filename in filenames:
#     myfile = open(filename, 'r')
#     print(myfile.read())


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     myfile = open(filename, 'w')
#     myfile.write("Hello " + filename[:-4])
#     myfile.close()

# for filename in filenames:
#     myfile = open(filename, 'r')
#     print(myfile.read())
#     myfile.close()

# myfile = open("members.txt", 'a+')
# myfile.seek(0)
# print(myfile.read())

# new_member = input("Add a new member: ") + '\n'

# myfile.write(new_member)
# myfile.seek(0)
# print(myfile.read())
# myfile.close()

# contents = ["Content for Document ++++++++++++++++++++++============"
#             "===========================", "Content for Report", 
#             "Content for Presentation"]
# filenames = ["doc.txt", "report.txt", "presentation.txt"]

#absolute_path = "C:\\GKP_Data\\Personal_Data\\TechLearn\\" \
#                "PyMegaCourse\\PyMegaVer2\\App1"

#relative_path = "\\Exp_files\\"

#file_path = absolute_path + relative_path

# for content, filename in zip(contents, filenames):
#     myfile = open(f"Exp_files\\{filename}", 'w')
#     myfile.write(content)
#     myfile.close()

# stand_alone = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#                "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" \
#                    "cccccccccccccccccccccccccccccccccccccc"
# print(stand_alone)

# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             row = f"{index+1}-{item}"
#             print(row, end='')                
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# #todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("\nEnter a todo: ") + "\n"
            
#             file = open("todos.txt", "r")
#             todos = file.readlines()
#             file.close()

#             todos.append(todo)
            
#             file = open("todos.txt", "w")
#             todos = file.writelines(todos)
#             file.close()

#         case 'show' | 'display':
#             file = open("todos.txt", 'r')
#             todos = file.readlines()
#             file.close()
#             show_todo(todos)

#         case 'edit':
#             show_todo(todos)
#             number = int(input("Type serial number of ToDo to be edited: "))
#             new_todo = input("Enter new ToDo item: ")
#             todos[number-1] = new_todo + '\n'
#             show_todo(todos)

#         case 'complete' :
#             show_todo(todos)
#             number = int(input("Type serial number of ToDo completed: "))
#             todos.remove(todos[number - 1])
#             show_todo(todos)

#         case 'exit':
#             break

#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")



# #Day 5

# buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
# for first, second, third in buttons:
#     print(first, second, third)

# ips = ['100.122.133.105', '100.122.133.111']
# for ip in ips:
#     index_num = int(input("Enter the index of the IP you want: "))
#     row = f"You chose {ips[index_num]}"
#     print(row)

# waiting_list = ["sen", "ben", "john"]
# waiting_list.sort()

# for index, name in enumerate(sorted(waiting_list)):
#     print_string = f"{index+1}.{name.capitalize()}"
#     print(print_string)
# print(waiting_list)


# def show_todo(todo_list):
#     if len(todo_list) != 0:
#         for index, item in enumerate(todo_list):
#             row = f"{index+1}-{item}"
#             print(row)
#             #print(index+1, ' - ', item)
#     else:
#         print("No Pending task to show")
#     return 0

# todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("\nEnter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             show_todo(todos)
#         case 'edit':
#             #show_todo(todos)
#             if len(todos) > 0:
#                 show_todo(todos)
                
#                 number = int(input("Type serial number of ToDo to be edited: "))
                
#                 new_todo = input("Enter new ToDo item: ")
#                 todos[number-1] = new_todo
#             else:
#                 print("There is no item to edit")    
#         case 'complete' :
#             show_todo(todos)
#             number = int(input("Type serial number of ToDo completed: "))
#             todos.remove(todos[number - 1])
#         case 'exit':
#             break
#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")

# #Day 4

# def show_todo(todo_list):
#     if len(todo_list) > 0:
#         for index, todo in enumerate(todo_list):
#             row = f"{index+1}-{todo}"
#             print(row)
#             #print(index+1, ' - ', todo)
#     else:
#         print("Todo list is empty")
#     return 0

# todos = []

# while True:
#     user_action = input("Type (A)dd, (S)how, (E)dit or e(X)it: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add' | 'A' | 'a':
#             todo = input("\nEnter a todo: ").upper()
#             todos.append(todo)
#         case 'show' | 'display' | 'S' | 's':
#             show_todo(todos)
#         case 'edit' | 'E' | 'e':
#             if len(todos) > 0:
#                 show_todo(todos)
#                 number = int(input("Type serial number of ToDo to be edited: "))
#                 new_todo = input("Enter new ToDo item: ")
#                 todos[number-1] = new_todo
#             else:
#                 print("There is no item to edit")    
             
#         case 'exit' | 'X' | 'x':
#             break
#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")


# #Day3

# todos = []

# while True:
#     user_action = input("Type add, show or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("\nEnter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             if len(todos) != 0:
#                 for todo in todos:
#                     print(todo)
#             else:
#                 print("There is no task in the list")        
#         case 'exit':
#             break
#         case misc :
#             print("Type add, show, exit only: ")

# print("Bye!")


# #Day2

# user_prompt = "Please enter your todo: "
# todos = []

# while True:
#     todo = input(user_prompt)
#     if todo.lower() == 'n':
#         break
#     else:
#         todos.append(todo)
#         print(todos)

# #Day1    
# user_prompt = "Please enter your todo: "
# todo_01 = input(user_prompt) 
# todo_02 = input(user_prompt)
# todo_03 = input(user_prompt)

# todos = [todo_01, todo_02, todo_03, "Gyaneshwar" ]
# print("\n")
# print(todos)

# print(type(todo_01))
# print(type(todos))
# print(type(user_prompt))
