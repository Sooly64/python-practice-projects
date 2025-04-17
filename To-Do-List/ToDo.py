# To-Do List Keeper
def addTask(task):
    with open("c:/Users/light/OneDrive/Desktop/FileHandling/bob.txt", "a") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(task)
    print("Task Added Successfully")
def showTasks():
    with open("c:/Users/light/OneDrive/Desktop/FileHandling/bob.txt" , "r") as file:
        content = file.readlines()
        for i in range(len(content)):
            print(f"Task {i + 1}: {content[i].strip()}")
def removeTasks(task_Index):
    with open("ToDos.txt", "r") as file:
        tasks = file.readlines()
    if 0 < task_Index <= len(tasks):
        removedTask = tasks.pop(task_Index - 1)
        with open("ToDos.txt", "w") as file:
            file.writelines(tasks)
        print(f"\"{removedTask}\" removed successfully!")
    else:
        print("Invalid Index!")

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
                removeTasks(int(taskIndexToRemove))
    elif command == "q":
        break
    else:
        print("Invalid Command, please try again!")