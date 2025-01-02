from modules.functions import *
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() #remove white space from input


    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)


    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos): #we iterrate over the list
            item = item.strip('\n') #or we can remove \n this way
            row = f"{index+1}-{item}"
            print(row)


    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif  user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            to_do_remove = todos[number-1].strip('\n') #we make this variable to show to the user which todo was deleted
            todos.pop(number-1)

            write_todos(todos)

            message = f'Todo {to_do_remove} was removed from the list'
            print(message)
        except IndexError:
            print("Todo with this number is not exist")

    elif 'exit' in user_action:
        break
    else:
        print('This command is not valid')


print("Bye")
