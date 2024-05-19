# Task Manager Application

Welcome to the Task Manager Application! This is a basic task manager written in Python, showcasing fundamental Python skills including modularization, file I/O operations, OOP, unit testing, and more.

## Features

This task manager allows for the following functionalities:
- **Account Management**:
  - Create an account as an employee or an admin.
  - Log in and log out, changing the "current_user".
- **Task Management**:
  - Differentiate access to certain functionalities based on user roles (employee or admin).
  - Create tasks with title and description, with status set as 'incomplete' by default.
  - Update task status to complete or back to incomplete.
  - Edit task descriptions.
  - Assign tasks to employees (admin only).
  - Delete tasks (admin only).

## Modules

### Main Module
- **main.py**: This is the main script which runs the program.

### Application Module
- **application.py**: Contains the user interface logic, displaying different menus based on user login status.

### Account Management Modules
- **create_account.py**: Logic for creating new employee or admin accounts and storing information in the database. Automatically logs the user in.
- **login.py**: Handles user login by matching input details with existing accounts in the database.

### Task Management Module
- **tasks_logic.py**: Contains the logic for all task operations, employing appropriate exception handling techniques.

### Data Models Module
- **objects.py**: Contains the necessary classes that form the basis of the task manager, i.e., the tasks and the users.

### Tests
- **tests/**: Directory containing unit tests for the program.

### Database
- **database/**: Directory containing text-based files that form the database where user and task information is stored.

### Requirements
- **requirements.txt**: Lists necessary dependencies for environment setup.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/task_manager.git
    cd task_manager
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage Instructions

1. **Run the Application**:
    ```sh
    python main.py
    ```

2. **Follow On-Screen Prompts**:
    - Create an account or log in.
    - Manage tasks based on your role (employee or admin).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

Thank you for using the Task Manager Application!
