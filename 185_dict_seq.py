# 185. Example - Constructing Dictionaries from Sequences

# list ans tuple to dict using zip 
subjects = ["Math", "Physics", "Chemistry"]
marks = (85, 90, 78)

# dictionary using zip()
report_card = dict(zip(subjects, marks))
print(report_card)

# using dictionary comprehension 
# add 5 mark as attendence
grade_card = {subj :mark+5 for subj,mark in zip(subjects,marks)}
print(grade_card)


# check grades A,B,C,D
grades = {
    subj: (
        "A" if mark >= 90 else
        "B" if mark >= 80 else
        "C" if mark >= 70 else
        "D"
    )
    for subj, mark in zip(subjects, marks)
}
print("GRades : ",grades)
