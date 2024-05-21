import create_account
import login
import tasks_logic


class TaskManagerApplication:
    def __init__(self):
        """Initialize the TaskManagerApplication instance."""
        self.version = "1.0"
        self.company_name = "Iqtidar"
        self.current_user = None
        self.all_tasks_file = "all_tasks.txt"
        self.display_menu()

    def display_menu(self):
        """Display the main menu for the task manager application and handle user input."""
        while True:
            if self.current_user:
                print(
                    f"\nWelcome, {self.current_user.first_name} {self.current_user.last_name}!"
                )
                print(
                    """What would you like to do?
                         1. Create a task
                         2. Edit a task description
                         3. Mark a task as complete
                         4. View all tasks
                         5. Assign a task to an employee (Admin only)
                         6. Delete a task (Admin only)
                         7. Logout
                         Enter your choice: """
                )
                choice = input()
                if choice == "1":
                    tasks_logic.create_task(self)
                elif choice == "2":
                    tasks_logic.edit_task(self)
                elif choice == "3":
                    tasks_logic.update_task_status(self)
                elif choice == "4":
                    tasks_logic.view_all_tasks(self)
                elif choice == "5":
                    tasks_logic.assign_task(self)
                elif choice == "6":
                    tasks_logic.delete_task(self)
                elif choice == "7":
                    self.current_user = None
                    print("Logged out successfully.")
                else:
                    print("Invalid choice. Please try again.")
            else:
                print(
                    """\nWelcome to the Task Manager!
                         What would you like to do?
                         1. Create an account
                         2. Log in
                         3. Exit
                         Enter your choice: """
                )
                choice = input()
                if choice == "1":
                    create_account.create_user_account(self)
                elif choice == "2":
                    login.login(self)
                elif choice == "3":
                    print("Exiting the Task Manager. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


def start_app():
    """Start the Task Manager application."""
    TaskManagerApplication()
