numStudents = int(input("Enter the number of students: "))
numExams = int(input("Enter the number of exams: "))
for student in range(1, numStudents+1):
    total = 0
    for exam in range(1, numExams+1):
        score = int(input("Enter the score for student " + str(student) + " for exam " + str(exam) + ": "))
        total += score
    print("The average exam score for student",(student),"is: ",round(total/numExams,2), "\n")
