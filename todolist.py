tasks = []

def Addtask():
    task = input("Enter the task :")
    tasks.append(task)
    print(f" Task `{task}` added to the list")

def Listtask():
    if not tasks:
        print("There is no task in your list")
    else:
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")

def Deletetask():
    Listtask()
    try:
        tasktodelete = int(input("Enter the # to delete the task :"))
        if(tasktodelete >=0 and tasktodelete < len(tasks)):
            tasks.pop(tasktodelete)
            print(f"Task to be removed sucessfully")
        else:
            print(f" Task to #{tasktodelete} is not found")
    except:
        print("Invalid Task")


        

if __name__ ==  "__main__":
    print("Welcome to do List " )
while True:
    print("\n")
    print("------------------------------")
    print("Select one of the following")
    print("1. Add task ")
    print("2. Delete task")
    print("3. List task")
    print("4. Exit")

    choice = int(input("Enter the choice :"))

    if(choice == 1):
        Addtask()
    elif(choice == 2):
        Deletetask()
    elif(choice == 3):
        Listtask()
    elif(choice == 4):
        print("Exit the To do list " )
        break
    else:
        print("Invalid Choice")
        
    
    
