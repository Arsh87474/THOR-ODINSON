marks = input("How many marks did you get?\n")
marks = float(marks)
grade = ""

if marks > 100 :
    print("sorry, you cannot score more than 100 marks in the exam")
    exit(0)
if marks > 90 :
    grade = "A+.Excellent"
elif marks > 80 :
    grade = "A. Amazing"
elif marks > 70 :
    grade = "B.Very good"
elif marks > 60 :
    grade = "C.Good enough"
elif marks >= 50 :
    grade = "D.Good try"
elif marks < 0:
    print("sorry, you cannot score less than 0 marks in the exam")
else :
    grade = "Failed.You can improve next time"

print(grade)
