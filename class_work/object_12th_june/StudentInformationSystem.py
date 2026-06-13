class Student:
    def __init__(self,studentName, rollNo, marks):
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
            exit()
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

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#------- Main Program ----------------------------------------------------------
#Ask the user to enter the account details
# Validate name
studentName = input("Enter Student Name: ")

if studentName.strip() == "":
    exit("Name cannot be empty.")

# Validate roll number
rollNo = int(input("Enter Roll Number: "))

if rollNo <= 0:
    exit("Invalid Roll Number! Roll Number must be positive.")

# Accept marks
marks = Student.accept_marks()      # if accept_marks is a class method


# Create object
student = Student(studentName, rollNo, marks)

#menu driven program to perform various operations on the account
while True:
    print(" 1 . Name of student ")
    print(" 2 Roll No of student")
    print(" 3 Marks of student")
    print(" 4 Total marks")
    print(" 5 Persentage of student")
    print(" 6 Exit")
    choice=int(input("Select operation: "))
    if choice == 1:
        student.display_Student_info()
    elif choice == 2:
        student.accept_roll_no()
    elif choice == 3:
        student.accept_marks()
    elif choice == 4:
        student.calculate_total()
    elif choice == 5:
        student.calculate_percentage()
    elif choice==5:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.")
    
        









    

    

