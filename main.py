import application

"""
WELCOME TO THE TASK MANAGER APPLICATION

This task manager allows for the following functionalities:
- Account Management:
  - Create an account as an employee or an admin.
  - Log in and log out, changing the "current_user".
- Task Management:
  - Differentiate access to certain functionalities based on user roles (employee or admin).
  - Create tasks with title and description, with status set as 'incomplete' by default.
  - Update task status to complete or back to incomplete.
  - Edit task descriptions.
  - Assign tasks to employees (admin only).
  - Delete tasks (admin only).

Find this project on https://github.com/javerria/task_manager

"""
if __name__ == "__main__":
    application.start_app()
