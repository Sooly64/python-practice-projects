# 📝 To-Do List Keeper

A simple command-line Python app that helps you keep track of tasks using file handling. Add, view, and remove tasks — all stored locally in a `.txt` file.

---

## 🚀 Features

- ✅ Add new tasks  
- 📋 View all tasks with task numbers  
- ❌ Remove tasks by index  
- 💾 Stores tasks persistently using file I/O
- 💬 Built in Comment detection to avoid lines of text that begin with # in the txt file

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
