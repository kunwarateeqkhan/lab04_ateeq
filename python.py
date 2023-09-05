class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary
def search_employee_data(employees):
    print("Search Options:")
    print("1. Search by Age")
    print("2. Search by Name")
    print("3. Search by Salary (>, <, <=, >=)")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        age = int(input("Enter the age to search: "))
        found_employees = [emp for emp in employees if emp.age == age]
    elif choice == 2:
        name = input("Enter the name to search: ")
        found_employees = [emp for emp in employees if name.lower() in emp.name.lower()]
    elif choice == 3:
        operator = input("Enter the operator (> < <= >=): ")
        salary = int(input("Enter the salary to compare: "))
        if operator == ">":
            found_employees = [emp for emp in employees if emp.salary > salary]
        elif operator == "<":
            found_employees = [emp for emp in employees if emp.salary < salary]
        elif operator == ">=":
            found_employees = [emp for emp in employees if emp.salary >= salary]
        elif operator == "<=":
            found_employees = [emp for emp in employees if emp.salary <= salary]
        else:
            print("Invalid operator!")
            return

    if found_employees:
        print("Results:")
        for emp in found_employees:
            print(f"Employee ID: {emp.employee_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")
employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]
search_employee_data(employees)
