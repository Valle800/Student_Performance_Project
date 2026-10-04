student_name = "Valle"
course = "Information science"
university = "Moi university"
english = 70
computer = 80
mathematics = 65
information_science = 75
total = english + computer + mathematics + information_science
average = total / 4
print("Student Name:", student_name)
print("Course:", course)
print("University:", university)
print("Total:", total)
print("Average:",average)
if average>= 70:
  grade = "A"
elif average>= 60:
  grade = "B"  
elif average>= 50:
  grade = "C"
elif average>= 40:
  grade = "D" 
else:
  grade = "F"
print("Grade:", grade)
if average >= 40:
    status = "pass"
else:
    status = "fail"
print("status:", status)








