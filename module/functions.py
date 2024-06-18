def parser(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet, 'inches':inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * .0254
    return meters


#function to get the todo list from file
def get_todos():
    """function to get the todo list from file.
       If todos.txt is not found, it returns an empty list  
    """
    try:
        with open('todos.txt', 'r') as myfile_local:
            todos_local = myfile_local.readlines()
            return todos_local
    except FileNotFoundError:
        print("File todos.txt is not found")
        return []


#function to write the todo list into a file
def write_todos(todos_local):
    with open('todos.txt', 'w') as myfile_local:
        myfile_local.writelines(todos_local)
    return 0

#function to display the todo list
def show_todo(todo_list):
    if todo_list:
        print("Current list of todo items")
        for index, item in enumerate(todo_list):
            item = item.rstrip('\n')
            row = f"{index+1}-{item}"
            print(row)
    else:
        print("No Pending task to show OR File ToDo.txt is not present")
    return 0

# Instructions to use program
def user_guidelines():
    print("Instruction for using todo Command Line Program")
    print("1. To add a todo item type <example: add watch movie>")
    print("2. To edit a todo item type <example: edit 5 i.e. todo item's serial number>")
    print("3. To remove a todo item type <example: completed 5 i.e. completed todo item's serial number>")
    print("4. To exit program type <exit>")
    input("Press any key to continue: ")
    return 0

# print(__name__)
if __name__ == "__main__":
    print("Hello from functions")
