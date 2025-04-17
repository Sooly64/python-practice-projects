# 📝 To-Do List Keeper

A simple command-line Python app that helps you keep track of tasks using file handling. Add, view, and remove tasks — all stored locally in a `.txt` file.

---

## 🚀 Features

- ✅ Add new tasks  
- 📋 View all tasks with task numbers  
- ❌ Remove tasks by index  
- 💾 Stores tasks persistently using file I/O  
- 💬 Built-in comment detection to avoid lines that begin with `#` in the task file

---

## 📂 How It Works

The app uses basic file operations to store and update tasks inside a `.txt` file on your local machine. It supports:

- Writing new tasks using **append mode**
- Reading all tasks and displaying them
- Removing specific tasks and updating the file

---

## 🛠️ Code Structure

```python
addTask(task)       # Adds a new task to the file  
showTasks()         # Displays all saved tasks  
removeTasks(index)  # Deletes a task by its number  
```

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Save the script as something like `todo_list.py`.
3. Make sure `ToDos.txt` exists in the path defined inside the code, or change the path to where you want to store tasks by copying the txt file as a path
4. Open a terminal and navigate to the folder with the script.
5. Run it using:

```bash
python todo_list.py
```

6. Use the commands:
   - `a` → add task  
   - `s` → show all tasks  
   - `r` → remove a task  
   - `q` → quit the program

---

