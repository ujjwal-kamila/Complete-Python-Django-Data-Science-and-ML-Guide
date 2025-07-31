# 166. Example - Calculating School Grades using the Ternary Operator

def letter_grade(marks):
    letter_grade= "A" if marks >= 90 else \
           "B" if marks >= 80 else \
           "C" if marks >= 70 else \
           "D" if marks >= 60 else "F"
    return letter_grade

# test case
print(letter_grade(75))
print(letter_grade(59))
print(letter_grade(91))

score = float(input("Enter your marks: "))
print(f"Your grade is: {letter_grade(score)}")
