print("Student Marks and Grade Checker")
marks = []
for subject in ["English", "Math", "Computer"]:
    while True:
        try:
            mark = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
total = sum(marks)
percentage = total / 300 * 100
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("--- Final Result ---")
print(f"Total: {total:g}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
