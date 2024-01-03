students_list = []
def add_student(reg_no, name, marks):
    stud_directory = {'Reg No.': reg_no, 'Name': name, 'Marks': marks}
    students_list.append(stud_directory)
    print(f"{name} added to the list")
def calculate_marks(student_marks):
    total_marks = sum(student_marks)
    average_marks = total_marks / len(student_marks)

    if average_marks >= 90:
        grade = 'A'
    elif 80 <= average_marks <= 89:
        grade = 'B'
    elif 70 <= average_marks <= 79:
        grade = 'C'
    elif 60 <= average_marks <= 69:
        grade = 'D'
    else:
        grade = 'NG'

    return total_marks, average_marks, grade

def display_students(register_no='ALL'):
    if register_no == 'ALL':
        print("Student Mark List- I MCA – Semester 1 (2023-24)")
        print("RegNo   Name   Total  Average   Grade")
        for student in students_list:
            total, average, grade = calculate_marks(student['Marks'])
            print(f"{student['Reg No.']}     {student['Name']}   {total}   {average}   {grade}")
    else:
        print("Enter Register Number:", register_no)
        print("Student Mark List- I MCA – Semester 1 (2023-24)")
        for student in students_list:
            if student['Reg No.'] == register_no:
                total, average, grade = calculate_marks(student['Marks'])
                print(f"Reg. No. :{student['Reg No.']}\nName : {student['Name']}\nTotal : {total}\nAverage : {average}\nGrade : {grade}")
                break
