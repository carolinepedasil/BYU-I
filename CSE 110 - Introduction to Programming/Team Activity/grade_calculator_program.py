grade_percentage = float(input("Enter your grade percentage: "))

letter = ""

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

last_digit = int(grade_percentage % 10)
sign = ""

if letter in ["A", "B", "C", "D"]:
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
    
if letter == "A" and last_digit == 10:
    letter = "A"
    sign = ""
elif letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")

if grade_percentage >= 70:
    print("Congratulations! You passed the course.")
else:
    print("Don't worry, keep trying for next time!")
