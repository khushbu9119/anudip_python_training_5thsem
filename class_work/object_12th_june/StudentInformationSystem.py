class Student:
    def __init__(self,studentName, rollNo, marks)
        self.studentName = studentName
        self.rollNo = rollNo
        self.marks = marks
    #Method to display the account details
    def display_Student_info(self):
        print("Student Name : ",self.studentName)
        print("Student Roll No. : ",self.rollNo)
        print("Student Marks : ",self.marks)

    def accept_roll_no(self):
        self.roll_no = int(input("Enter Roll Number: "))
        if self.roll_no > 0:
            break
        else:
            print("Invalid Roll Number! Roll Number must be positive.")
    # accept marks
    def accept_marks(self):
        self.marks = []
        for i in range(3):
            mark = float(input(f"Enter Marks of Subject {i+1}: "))
            self.marks.append(mark)
    # calculate total marks
    def calculate_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3
        return self.total
    # calculate persentage
    def calculate_percentage(self):
        self.percentage = (self.total / len(self.marks)) 
    
   # Display complete student detail
    def display_report(self):
        print("----- Student Report -----")
        print("Name       :", self.name)
        print("Roll No.   :", self.roll_no)
        print("Marks      :", self.marks)
        print("Total Marks:", self.total)
        print("Percentage :", round(self.percentage, 2), "%")
    #create object of student class
student = Student(studentName, rollNo, marks)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#------- Main Program ----------------------------------------------------------
#Ask the user to enter the account details
name=input("Enter the Student's name: ")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
#








    

    

