import Student_Mark
num_students = int(input("Enter Number of Students: "))
for i in range(1, num_students + 1):
    print(f"Enter Details of Student {i}: ")
    reg_no = input("Enter Student Reg. No.: ")
    name = input("Enter Student Name: ")
    marks_input = input("Enter Marks separated by spaces: ")
    marks = list(map(int, marks_input.split()))
    Student_Mark.add_student(reg_no, name, marks)
display_option = input("To Display Student Details -> For All Press 'a' or For Specific Press 's': ")
if display_option == 'a':
    Student_Mark.display_students()
elif display_option == 's':
    specific_reg_no = input("Enter Register Number: ")
    Student_Mark.display_students(specific_reg_no)
else:
    print("Not Valid")