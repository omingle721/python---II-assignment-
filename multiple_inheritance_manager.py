# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Employee class
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Manager class inheriting from Person and Employee
class Manager(Person, Employee):

    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_employee()
        print("Department:", self.department)


# Creating object
manager1 = Manager("Om", 19, 101, 50000, "IT")

# Display details
manager1.display_manager()