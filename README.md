# Student Academic Eligibility & Scholarship System

## Overview

This is a beginner-friendly Python project that evaluates a student's academic performance, exam eligibility, and scholarship eligibility based on the given information.

The project uses basic Python concepts such as variables, user input, type conversion, conditional statements, logical operators, nested if statements, ternary expressions, and None handling.

## Features

- Collects student information
- Accepts attendance and subject marks
- Calculates total marks
- Calculates percentage
- Determines Pass or Fail
- Assigns a grade
- Checks exam eligibility
- Checks scholarship eligibility
- Handles optional scholarship codes
- Performs special scholarship review

## Conditions Used

### Pass / Fail

A student passes when:

- Maths marks are at least 40
- Science marks are at least 40
- Python marks are at least 40
- Attendance is at least 75%

### Grade

| Percentage | Grade |
|---|---|
| 90 and above | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| Below 40 | F |

### Exam Eligibility

A student is eligible when:

- Age is at least 18
- Student is a citizen
- Student has an ID
- Student is not suspended

### Scholarship Eligibility

A student is eligible when:

- The student has passed
- The student is a citizen
- Percentage is at least 75%

## Python Concepts Used

- Variables
- `input()`
- `int()` and `float()`
- Strings
- Boolean values
- Arithmetic operators
- Comparison operators
- Logical operators
- `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Ternary / conditional expression
- Truthy and Falsy values
- `None`
- `is None`
- Boundary conditions

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run `student_eligibility.py`.
5. Enter the requested student information.

## Sample Input

```text
yasaswini
23
yes
yes
no
92
89
94
96
yes
```

## Sample Output

```text
===== STUDENT REPORT =====
Student Name: yasaswini
Age: 23
Citizenship: True
Has ID: True
Is Suspended: False
Premium Member: True
Attendance: 92.0
Maths: 89
Science: 94
Python: 96
Total Marks: 279
Percentage: 93.0
Grade: A
Final Result: Pass
Exam Status: Exam Eligible
Scholarship Status: Scholarship Eligible
No Scholarship Code
Special Review: Special Scholarship Review
```

## Testing

The project was tested using different boundary and real-world cases, including:

- Marks exactly 40
- Marks below 40
- Attendance exactly 75
- Attendance below 75
- Percentage exactly 90
- Suspended student
- Non-citizen student
- Student with a scholarship code
- Student without a scholarship code

## Project Structure

```text
student-eligibility-scholarship-system/
├── student_eligibility.py
├── README.md
└── test_cases.md
```

## Future Improvements

Possible future versions can include:

- Functions for better code organization
- File handling
- CSV student records
- Database integration
- Input validation
- A graphical or web interface