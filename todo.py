import sys
from datetime import datetime

try:
    option = sys.argv[1]
except IndexError:
    option = "help" 

if option=='add':
    try:
        with open('todo.txt','a') as todoFile:
            todoFile.write(str(sys.argv[2])+"\n")
            print('Added todo: "{}"'.format(sys.argv[2]))
            todoFile.close()
    except IndexError:
        print('Error: Missing todo string. Nothing added!')

elif option=='ls':
    try:
        with open('todo.txt','r') as todoFile:
            todoItems=list(todoFile)
            if len(todoItems)>0:
                for i in range(len(todoItems),0,-1):
                    print("[{}] {}".format(i,todoItems[i-1]),end="")
            else:
                raise FileNotFoundError()
    except FileNotFoundError:
        print('There are no pending todos!')

elif option=='help':
    help = """Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"""
    print (help)

elif option=='del':
    try:
        index = int(sys.argv[2])
        with open('todo.txt','r') as oldTodo:
            todoItems=list(oldTodo)
            try:
                if index<=0: raise IndexError
                del todoItems[index-1]
                with open('todo.txt','w') as newTodo:
                    for item in todoItems:
                        newTodo.write(item)
                    newTodo.close()
                    print("Deleted todo #{}".format(index))
            except IndexError:
                print('Error: todo #{} does not exist. Nothing deleted.'.format(index))        
            oldTodo.close()
    except IndexError:
        print("Error: Missing NUMBER for deleting todo.")
    except FileNotFoundError:
        print('There are no pending todos!')

elif option=='done':
    try:
        index = int(sys.argv[2])
        with open('todo.txt','r') as todoFile:
            todoItems=list(todoFile)
            try:
                if index<=0: raise IndexError
                todo=todoItems[index-1]
                del todoItems[index-1]
                with open('done.txt','a') as doneFile:
                    doneFile.write('x {} {}'.format(datetime.today().strftime('%Y-%m-%d'),todo))
                with open('todo.txt','w') as newTodo:
                    for item in todoItems:
                        newTodo.write(item)
                    newTodo.close()
                print("Marked todo #{} as done.".format(index))

            except IndexError:
                print('Error: todo #{} does not exist.'.format(index))

    except IndexError:
        print('Error: Missing NUMBER for marking todo as done.')
    except FileNotFoundError:
        print('There are no pending todos!')

elif option=='report':
    try:
        with open('todo.txt','r') as pendingTodo:
            pending=len(list(pendingTodo))
        with open('done.txt','r') as completedTodo:
            completed=len(list(completedTodo))
        date=datetime.today().strftime('%Y-%m-%d')
        print("{} Pending : {} Completed : {}".format(date,pending,completed))
    except FileNotFoundError:
        print('There are no pending todos!')