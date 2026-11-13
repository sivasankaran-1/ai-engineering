class Employee:
    def __init__(self, name, employeeid, salary):
        self.name = name
        self.employeeid = employeeid
        self.salary = salary

    def employee_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employeeid}")
        print(f"Salary: {self.salary}")

    def increase_salary(self, percentage):
        return self.salary + percentage

employee1 = Employee("siva", 145, 222)

employee1.employee_details()
employee1.increase_salary(10)



