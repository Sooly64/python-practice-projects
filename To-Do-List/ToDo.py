# To-Do List Keeper

FILE_PATH = "ToDos.txt"

def addTask(task):
    with open(FILE_PATH, "a") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(task)
    print("Task Added Successfully")

def showTasks():
    with open(FILE_PATH, "r") as file:
        content = file.readlines()
        lineNumber = 1
        for line in content:
            if not line.strip().startswith("#") and line.strip() != "":
                print(f"Task {lineNumber}: {line.strip()}")
                lineNumber += 1

def removeTasks(task_Index):
    try:
        with open(FILE_PATH, "r") as file:
            tasks = file.readlines()
        if 0 < task_Index <= len(tasks):
            removedTask = tasks.pop(task_Index - 1).strip()
            with open(FILE_PATH, "w") as file:
                file.writelines(tasks)
            print(f"\"{removedTask}\" removed successfully!")
        else:
            print("Invalid Index!")
    except ValueError:
        print("Please enter a valid number!")

print("Welcome to your To-Do List")
while True:
    command = input("Enter your command, a (add), s (show), r (remove), or q (quit): ")
    if command == "a":
        while True:
            task = input("Enter a task to add, or \"exit\" to exit: ")
            if task == "exit":
                break
            else:
                addTask(task)
    elif command == "s":
        showTasks()
        print("Tasks Shown Successfully!")
    elif command == "r":
        while True:
            taskIndexToRemove = input("Enter a task number to remove, or \"exit\" to exit: ")
            if taskIndexToRemove == "exit":
                break
            else:
                try:
                    removeTasks(int(taskIndexToRemove))
                except ValueError:
                    print("Please enter a valid number!")
    elif command == "q":
        break
    else:
        print("Invalid Command, please try again!")
