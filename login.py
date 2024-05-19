from objects import Employee, AdminUser


def login(app):
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Check if the user is an admin
    if is_admin(email, password):
        print("Login successful as Admin!")
        app.current_user = load_user_from_file("all_admin.txt", email)
        return

    # Check if the user is an employee
    if is_employee(email, password):
        print("Login successful as Employee!")
        app.current_user = load_user_from_file("all_employees.txt", email)
        return

    print("Login failed. Invalid email or password.")


def is_admin(email, password):
    with open("all_admin.txt", "r") as file:
        for line in file:
            admin_data = line.strip().split(",")
            if admin_data[2] == email and admin_data[3] == password:
                return True
    return False


def is_employee(email, password):
    with open("all_employees.txt", "r") as file:
        for line in file:
            employee_data = line.strip().split(",")
            if employee_data[2] == email and employee_data[3] == password:
                return True
    return False


def load_user_from_file(filename, email):
    with open(filename, "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            if user_data[2] == email:
                if filename == "all_admin.txt":
                    return AdminUser(
                        user_data[0], user_data[1], user_data[2], user_data[3]
                    )
                elif filename == "all_employees.txt":
                    return Employee(
                        user_data[0], user_data[1], user_data[2], user_data[3]
                    )
    return None
