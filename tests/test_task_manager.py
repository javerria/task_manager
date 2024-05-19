import unittest
from task_manager import objects


class TestTaskManager(unittest.TestCase):

    def test_task_initialization(self):
        """Test that a Task object is initialized correctly."""
        task_name = "Test Task"
        task_description = "This is a test task description"
        task = objects.Task(task_name, task_description)

        self.assertEqual(task.task_name, task_name)
        self.assertEqual(task.task_description, task_description)
        self.assertFalse(task.task_is_complete)

    def test_employee_initialization(self):
        """Test that an Employee object is initialized correctly."""
        first_name = "John"
        last_name = "Doe"
        email = "johndoe@example.com"
        password = "securepassword"

        employee = objects.Employee(first_name, last_name, email, password)

        self.assertEqual(employee.first_name, first_name)
        self.assertEqual(employee.last_name, last_name)
        self.assertEqual(employee.email, email)
        self.assertEqual(employee.password, password)

    def test_admin_user_initialization(self):
        """Test that an AdminUser object is initialized correctly."""
        first_name = "Jane"
        last_name = "Doe"
        email = "janedoe@example.com"
        password = "adminpassword"

        admin_user = objects.AdminUser(first_name, last_name, email, password)

        self.assertEqual(admin_user.first_name, first_name)
        self.assertEqual(admin_user.last_name, last_name)
        self.assertEqual(admin_user.email, email)
        self.assertEqual(admin_user.password, password)

    def test_task_mark_as_complete(self):
        """Test that a task can be marked as complete."""
        task_name = "Test Task"
        task_description = "This is a test task description"
        task = objects.Task(task_name, task_description)

        # Ensure task is initially incomplete
        self.assertFalse(task.task_is_complete)

        # Mark the task as complete
        task.task_is_complete = True

        # Verify task status
        self.assertTrue(task.task_is_complete)

    def test_employee_string_representation(self):
        """Test the string representation of an Employee object."""
        first_name = "John"
        last_name = "Doe"
        email = "johndoe@example.com"
        password = "securepassword"

        employee = objects.Employee(first_name, last_name, email, password)

        expected_str = f"Name: {first_name} {last_name}, email: {email}"
        self.assertEqual(str(employee), expected_str)


if __name__ == "__main__":
    unittest.main()
