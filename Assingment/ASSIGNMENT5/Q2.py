# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num_students = int(input("Enter number of students: "))

all_percentages = 0
for student in range(1, num_students + 1):
    print(f"Enter marks for student {student}:")
    marks = 0
    for subject in range(1, 6):
        mark = float(input(f"Subject {subject}: "))
        marks += mark
    percentage = marks / 5
    print(f"Percentage for student {student}: {percentage}%")
    all_percentages += percentage
average_percentage = all_percentages / num_students
print(f"Average percentage of students: {average_percentage}%")