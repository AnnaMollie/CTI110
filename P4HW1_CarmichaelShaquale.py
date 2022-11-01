# CTI-110
# P4HW1 - Grades
# Shaquale Carmichael 
# 11/01/2022
  

grades = [] 


for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)


print("The grades are:", grades)
print("The highest grade is: ", max(grades))
print("The lowest grade is: ", min(grades))

total = sum(grades)
count = len(grades)
average = total / count
print("The total is: ", total)
print("The average is: ", average)

print
