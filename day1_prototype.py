# Smart Student Performance Prediction System
# Day 1 - Python Prototype
# Without Machine Learning and Tkinter


# -----------------------------------------
# 1. Get Student Data
# -----------------------------------------

student_name = input("Enter Student Name: ")

attendance = float(input("Enter Attendance (%): "))

study_hours = float(input("Enter Study Hours per Day: "))

internal_marks = float(input("Enter Internal Marks (%): "))

assignment_completion = float(
    input("Enter Assignment Completion (%): ")
)


# -----------------------------------------
# 2. Convert Study Hours into Score
# -----------------------------------------

study_hours_score = min((study_hours / 8) * 100, 100)


# -----------------------------------------
# 3. Calculate Performance Score
# -----------------------------------------

performance_score = (
    attendance * 0.20
    + study_hours_score * 0.20
    + internal_marks * 0.40
    + assignment_completion * 0.20
)


# -----------------------------------------
# 4. Determine Performance Level
# -----------------------------------------

if performance_score >= 80:
    performance_level = "EXCELLENT"

elif performance_score >= 65:
    performance_level = "GOOD"

elif performance_score >= 50:
    performance_level = "AVERAGE"

else:
    performance_level = "AT RISK"


# -----------------------------------------
# 5. Generate Recommendation
# -----------------------------------------

if performance_level == "EXCELLENT":

    recommendation = (
        "Excellent performance. Maintain your current study "
        "pattern and continue regular practice."
    )

elif performance_level == "GOOD":

    recommendation = (
        "Maintain attendance and continue regular study."
    )

elif performance_level == "AVERAGE":

    recommendation = (
        "Increase study hours, improve assignment completion, "
        "and focus on internal assessments."
    )

else:

    recommendation = (
        "Improve attendance, increase study hours, complete "
        "assignments regularly, and seek academic guidance."
    )


# -----------------------------------------
# 6. Display Result
# -----------------------------------------

print("\n========== STUDENT PERFORMANCE RESULT ==========")

print("Student Name:", student_name)

print("Performance Score:", round(performance_score, 2))

print("Performance Level:", performance_level)

print("Recommendation:", recommendation)

print("=================================================")