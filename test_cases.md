# Test Cases

This document contains the test cases used to verify the Student Academic Eligibility & Scholarship System.

## Test Case 1 — Normal Successful Student

### Input

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

### Expected Result

- Grade: A
- Final Result: Pass
- Exam Status: Exam Eligible
- Scholarship Status: Scholarship Eligible
- Special Review: Special Scholarship Review

### Status

✅ Passed

---

## Test Case 2 — Exact Passing Boundary

This test checks whether the program accepts the minimum passing values.

### Input

```text
student1
20
yes
yes
no
75
40
40
40
no
```

### Expected Result

- Total Marks: 120
- Percentage: 40.0
- Grade: D
- Final Result: Pass
- Exam Status: Exam Eligible
- Scholarship Status: Scholarship Not Eligible
- Special Review: No Special Scholarship Review

### Status

✅ Passed

---

## Test Case 3 — Attendance Below Passing Boundary

This test checks attendance just below the required 75%.

### Input

```text
student2
20
yes
yes
no
74
40
40
40
no
```

### Expected Result

- Final Result: Fail

### Status

✅ Passed

---

## Test Case 4 — One Subject Below 40

This test checks whether a student fails when one subject is below the minimum required mark.

### Input

```text
student3
20
yes
yes
no
80
39
90
90
no
```

### Expected Result

- Final Result: Fail

### Status

✅ Passed

---

## Test Case 5 — Suspended Student

This test checks whether a suspended student is denied exam eligibility.

### Input

```text
student4
23
yes
yes
yes
90
80
90
90
yes
```

### Expected Result

- Final Result: Pass
- Exam Status: Exam Not Eligible

### Status

✅ Passed

---

## Test Case 6 — Non-Citizen Student

This test checks the effect of citizenship on exam and scholarship eligibility.

### Input

```text
student5
23
no
yes
no
90
80
90
90
no
```

### Expected Result

- Final Result: Pass
- Exam Status: Exam Not Eligible
- Scholarship Status: Scholarship Not Eligible

### Status

✅ Passed

---

## Test Case 7 — Scholarship Code Provided

This test checks whether a provided scholarship code is displayed correctly.

### Input

```text
student6
23
yes
yes
no
85
80
80
85
no
SCH123
```

### Expected Result

- Scholarship Status: Scholarship Eligible
- Scholarship Code: SCH123

### Status

✅ Passed

---

## Test Case 8 — No Scholarship Code

This test checks the handling of an empty scholarship code.

### Expected Result

```text
No Scholarship Code
```

### Status

✅ Passed

---

## Testing Summary

| Test Case | Scenario | Status |
|---|---|---|
| 1 | Normal successful student | ✅ Passed |
| 2 | Exact passing boundary | ✅ Passed |
| 3 | Attendance below 75% | ✅ Passed |
| 4 | Subject mark below 40 | ✅ Passed |
| 5 | Suspended student | ✅ Passed |
| 6 | Non-citizen student | ✅ Passed |
| 7 | Scholarship code provided | ✅ Passed |
| 8 | No scholarship code | ✅ Passed |

## Conclusion

The project was tested using normal cases, boundary conditions, and different eligibility scenarios. All documented test cases passed successfully.