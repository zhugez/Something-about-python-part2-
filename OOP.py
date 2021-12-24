class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(',')
        age = int(age)
        return cls(name, age)
    @staticmethod
    def is_adult(age):
        return age >= 18
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    @classmethod
    def from_string(cls, student_str):
        name, age, major = student_str.split(',')
        age = int(age)
        return cls(name, age, major)
    @staticmethod
    def is_adult(age):
        return age >= 21
class Employee(Person):
    def __init__(self, name, age, title, salary):
        super().__init__(name, age)
        self.title = title
        self.salary = salary
    @classmethod
    def from_string(cls, employee_str):
        name, age, title, salary = employee_str.split(',')
        age = int(age)
        salary = int(salary)
        return cls(name, age, title, salary)
    @staticmethod
    def is_adult(age):
        return age >= 21
class Manager(Person):
    def __init__(self, name, age, title, salary, employees=None):
        super().__init__(name, age)
        self.title = title
        self.salary = salary
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    @classmethod
    def from_string(cls, manager_str):
        name, age, title, salary = manager_str.split(',')
        age = int(age)
        salary = int(salary)
        return cls(name, age, title, salary)
    @staticmethod
    def is_adult(age):
        return age >= 21
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def __str__(self):
        return f'{self.name} - {self.title} - {self.salary}'

class Main:
    def __init__(self):
        pass
    def main(self):
        student_str = 'John,35,Computer Science'
        employee_str = 'John,35,Manager,100000'
        manager_str = 'John,35,Manager,100000,John,35,Manager,100000'
        student = Student.from_string(student_str)
        employee = Employee.from_string(employee_str)
        manager = Manager.from_string(manager_str)
        print(manager.add_employee(employee))
        print(manager.remove_employee(employee))
        print(manager.add_employee(student))

if __name__ == '__main__':
    Main().main()
