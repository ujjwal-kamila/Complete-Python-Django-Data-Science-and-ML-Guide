# 153. Practice - Working with Multiple if Statements

# create a student report with all grades also include 

def student_report(name, marks, attendance):
    print(f"\n Report Card for {name}")
    
    # Check attendance
    if attendance < 75:
        print("Low attendance! ")
        return

    # Grades
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # Result
    if grade == 'F':
        print(f"Failed... Grade: {grade}")
    else:
        print(f"Passed :)  Grade: {grade}")
    
    if marks > 95 and attendance > 80:
        print(" You are a topper!")
    elif marks < 60:
        print(" Please study harder next time.")

# Test case
student_report("Ujjwal", 96, 81)
student_report("Rahul", 59, 78)
student_report("Aashiq", 91, 80)


