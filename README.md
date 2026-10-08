# Command-Line To-Do Application

## Description
This is a simple **command-line To-Do application** written in Python. It allows users to manage their tasks directly from the terminal.
Tasks are stored in a **Python list**, and separate functions are used for each operation.

## Features
- Add new tasks
- View all tasks
- Update existing tasks
- Remove tasks
- Exit the application
- Handles invalid menu choices
- Handles invalid task numbers
- Prevents the program from crashing when invalid numbers are entered

## How It Works
The application displays a menu:
```text
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Update Task
4. Remove Task
5. Exit
```

The user selects an option by entering a number from **1 to 5**.
### 1. Add Task
The user enters a task, which is added to the `tasks` list.
Example:
```text
Enter task: Complete Science homework
Task added successfully!
```

### 2. View Tasks
Displays all tasks currently stored in the list.
Example:
```text
1. Complete Science homework
2. Practice Python
3. Study Maths
```

### 3. Update Task
The user selects a task number and enters the new task.
Example:
```text
Enter task number to update: 2
Enter updated task: Practice Python loops
Task updated successfully!
```

### 4. Remove Task
The user selects a task number, and that task is removed from the list.
Example:
```text
Enter task number to remove: 1
Task removed successfully!
```

### 5. Exit
Ends the program.
```text
Goodbye!
```

## Invalid Input Handling
The program handles invalid menu choices:
```text
Enter your choice (1-5): 8
Invalid menu choice. Please enter a number from 1 to 5.
```
It also handles invalid task numbers and non-numeric input without crashing the program.

## Python Concepts Used
- Lists
- Functions
- `while` loop
- `for` loop
- `if`, `elif`, and `else`
- `input()`
- `append()`
- `pop()`
- List indexing
- `enumerate()`
- `try-except`
- `ValueError`

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run
Save the program as:
```text
todo.py
```

Then run:
```text
python todo.py
```

The application will open in the terminal and display the To-Do menu.
