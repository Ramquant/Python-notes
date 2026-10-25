score = 85

if score >= 90:
    grade = "A"
    status = "Distinction"
elif score >= 75:
    grade = "B"
    status = "First Class"
elif score >= 50:
    grade = "C"
    status = "Pass"
else:
    grade = "F"
    Status = "Needs Improvement"

print(f"Final Score: {score}\nGrade Awarded: {grade}\nStatus: {status}")
