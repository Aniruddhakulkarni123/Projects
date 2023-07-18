student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print (f"Number of Student = {number_of_student}")

Average_Height = round(total_height / number_of_student)
print(f"Average Height = {Average_Height}")