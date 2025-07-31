# Grade system 
marks = int(input("Enter your marks (0–100): "))

if marks < 0 or marks > 100:
    print("Invalid marks entered.")
elif marks >= 90:
    print("Grade: A+")
    print("Excellent!")
elif marks >= 80:
    print("Grade: A")
    print("Very good!")
elif marks >= 70:
    print("Grade: B+")
    print("Good..")
elif marks >= 60:
    print("Grade: B")
    print("Fair..")
elif marks >= 50:
    print("Grade: C")
    print("Below average..")
elif marks >= 35:
    print("Grade: D")
    print("Passed..")
else:
    print("Grade: F")
    print("Failed..")