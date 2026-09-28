# Student Academic Eligibility & Scholarship System

# -----------------------------
# 1. Student Information
# -----------------------------

student_name = input()
age = int(input())

citizenship = input().lower() == "yes"
has_id = input().lower() == "yes"
is_suspended = input().lower() == "yes"

is_premium = input().lower() == "yes"


# -----------------------------
# 2. Attendance and Marks
# -----------------------------

attendance = float(input())

maths = int(input())
science = int(input())
python_marks = int(input())


# -----------------------------
# 3. Scholarship Code
# -----------------------------

scholarship_code = input()

if scholarship_code == "":
    scholarship_code = None


# -----------------------------
# 4. Total and Percentage
# -----------------------------

total_marks = maths + science + python_marks
percentage = total_marks / 3


# -----------------------------
# 5. Pass / Fail
# -----------------------------

if maths >= 40 and science >= 40 and python_marks >= 40 and attendance >= 75:
    result = "Pass"
else:
    result = "Fail"


# -----------------------------
# 6. Grade
# -----------------------------

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"


# -----------------------------
# 7. Exam Eligibility
# -----------------------------

if age >= 18 and citizenship and has_id and not is_suspended:
    exam_status = "Exam Eligible"
else:
    exam_status = "Exam Not Eligible"


# -----------------------------
# 8. Scholarship Eligibility
# -----------------------------

if result == "Pass":
    if citizenship:
        if percentage >= 75:
            scholarship_status = "Scholarship Eligible"
        else:
            scholarship_status = "Scholarship Not Eligible"
    else:
        scholarship_status = "Scholarship Not Eligible"
else:
    scholarship_status = "Scholarship Not Eligible"


# -----------------------------
# 9. Scholarship Code Status
# -----------------------------

if scholarship_code is None:
    code_status = "No Scholarship Code"
else:
    code_status = "Scholarship Code: " + scholarship_code


# -----------------------------
# 10. Special Scholarship Review
# -----------------------------

if is_premium or percentage >= 90:
    special_review = "Special Scholarship Review"
else:
    special_review = "No Special Scholarship Review"


# -----------------------------
# 11. Final Output
# -----------------------------

print()
print("===== STUDENT REPORT =====")

print("Student Name:", student_name)
print("Age:", age)
print("Citizenship:", citizenship)
print("Has ID:", has_id)
print("Is Suspended:", is_suspended)
print("Premium Member:", is_premium)

print("Attendance:", attendance)
print("Maths:", maths)
print("Science:", science)
print("Python:", python_marks)

print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
print("Final Result:", result)

print("Exam Status:", exam_status)
print("Scholarship Status:", scholarship_status)
print(code_status)
print("Special Review:", special_review)