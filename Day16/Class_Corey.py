# Python Object-Oriented Programming
# Employee = has attributes and methods (eg. name, email, position_title, pay)

# Create blueprient name = Employeefor creating instances.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        # return "{} {}".format(self.first, self.last)
        return self.first + " " + self.last


emp_1 = Employee("Jack", "Ma", 5000)  # unique instance of the Employee class
emp_2 = Employee("Cody", "Lee", 1000)  # unique instance of the Employee class

# print(emp_1)  # different location in the memory
# print(emp_2)

print(emp_1.email) # take emp_1 instance by the method
print(Employee.fullname(emp_2))
# print full name without creating method inside a class
print("{} {}".format(emp_1.first, emp_1.last))
print(f"Name printed using method inside the class:\n{emp_2.fullname()}")
