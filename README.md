# CLI To-Do App

A simple command-line To-Do application built with Python.

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Set optional deadlines and priorities
- Persistent storage using JSON

## Tech Stack

- Python
- JSON

## Project Structure

```text
todo-app/
├── todo.py
├── .gitignore
└── README.md
```

> `tasks.json` is generated automatically on first run and excluded from Git via `.gitignore`.

## Getting Started

```bash
git clone https://github.com/Ujjwal-nayan/todo-app.git
cd todo-app
python todo.py
```

## What I Learned

- Reading from and writing to JSON files
- Organizing code using functions
- CRUD operations with input validation
- Defensive error handling (missing files, invalid input, variable shadowing)
- Structuring a small Python project

## Future Improvements

- Store data using SQLite instead of JSON
- Add task categories
- Filter and sort tasks
- Build a graphical or web interface

## Author

**Ujjwal Nayan**  
GitHub: https://github.com/Ujjwal-nayan
