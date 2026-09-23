print("=====WELCOME TO THE CLASS GRADE ANALYZER=====")
total_marks=0
student_count=0
passed_count=0
highest_score=0
print("Enter the marks of students (between 0 and 100) and Marks Should be in Integer Format.")
print("Enter 'done' when you are finished entering marks.")
while True:
    User_Input=input(f"Enter Marks for the student {student_count+1} (or done):")
    if User_Input.lower()=='done':
        break
    Marks=int(User_Input)
    if Marks<0 or Marks>100:
        print("Invalid Marks!! Please Enter Marks Between 0 and 100.")
        continue
    else:
        total_marks+=Marks
        student_count+=1
        if Marks>=40:
            passed_count+=1
        if Marks>highest_score:
            highest_score=Marks
print("=====CLASS GRADE ANALYZER RESULTS=====")
if student_count>0:
    average_marks=total_marks/student_count
    print(f"Total Students: {student_count}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Number of Students Passed: {passed_count}")
    print(f"Highest Score: {highest_score}")
    print(f"Pass Percentage: {(passed_count/student_count)*100:.2f}%")
else:
    print("No Student Marks Entered. Please Enter Marks to Analyze The Class Performance.")
