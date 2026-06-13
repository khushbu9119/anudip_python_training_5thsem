class Employee:
    
    # Constructor
    def __init__(self, emp_id, name, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary

    # Display employee details
    def display_details(self):
        print("\nEmployee Details")
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("Monthly Salary : ₹", self.monthly_salary)

    # Calculate annual salary
    def annual_salary(self):
        return self.monthly_salary * 12

    # Increase salary by percentage
    def increase_salary(self, percentage):
        self.monthly_salary += (self.monthly_salary * percentage) / 100


# Input
emp_id = int(input("Enter Employee ID: "))
if emp_id<0:
    exit("Invalid ID ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Monthly Salary: "))

# Object Creation
emp = Employee(emp_id, name, salary)

# Display Details
emp.display_details()

# Annual Salary
print("Annual Salary : ₹", emp.annual_salary())

# Salary Increment
percent = float(input("\nEnter Salary Increase Percentage: "))
emp.increase_salary(percent)

print("Updated Salary : ₹", emp.monthly_salary)