class Task:
    def __init__(self, task_name, task_description, task_is_complete=False):
        """Initialize a new Task instance.

        Args:
            task_name (str): The name of the task.
            task_description (str): A brief description of the task.
            task_is_complete (bool, optional): The completion status of the task. Defaults to False.
        """
        self.task_name = task_name
        self.task_description = task_description
        self.task_is_complete = task_is_complete

    def __str__(self):
        """Return a string representation of the Task instance.

        Returns:
            str: A string containing the task's title, description, and completion status.
        """
        return f"Task title: {self.task_name}, Description: {self.task_description}, Status: {'Complete' if self.task_is_complete else 'Incomplete'}"


class Employee:
    def __init__(self, first_name, last_name, email, password):
        """Initialize a new Employee instance.

        Args:
            first_name (str): The first name of the employee.
            last_name (str): The last name of the employee.
            email (str): The email address of the employee.
            password (str): The password for the employee's account.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        """Return a string representation of the Employee instance.

        Returns:
            str: A string containing the employee's full name and email address.
        """
        return f"Name: {self.first_name} {self.last_name}, email: {self.email}"


class AdminUser(Employee):
    def __init__(self, first_name, last_name, email, password):
        """Initialize a new AdminUser instance.

        Args:
            first_name (str): The first name of the admin user.
            last_name (str): The last name of the admin user.
            email (str): The email address of the admin user.
            password (str): The password for the admin user's account.
        """
        super().__init__(first_name, last_name, email, password)

    def __str__(self):
        """Return a string representation of the AdminUser instance.

        Returns:
            str: A string containing the admin user's full name and email address, prefixed with 'Admin'.
        """
        return f"Admin: {super().__str__()}"
