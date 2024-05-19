class Task:
    def __init__(self, task_name, task_description, task_is_complete=False):
        self.task_name = task_name
        self.task_description = task_description
        self.task_is_complete = task_is_complete

    def __str__(self):
        return f"Task title: {self.task_name}, Description: {self.task_description}, Status: {'Complete' if self.task_is_complete else 'Incomplete'}"


class Employee:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, email: {self.email}"


class AdminUser(Employee):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)

    def __str__(self):
        return f"Admin: {super().__str__()}"
