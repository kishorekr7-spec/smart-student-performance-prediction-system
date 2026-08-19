import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("900x650")
root.configure(bg="#F2F2F2")

def predict_performance():
    student_id = entry_student_id.get()
    student_name = entry_student_name.get()
    attendance = entry_attendance.get()
    study_hours = entry_study_hours.get()
    internal_marks = entry_internal_marks.get()
    assignment = entry_assignment.get()
    previous_score = entry_prev_score.get()

    if not student_id or not student_name:
        messagebox.showwarning(
            "Missing Information",
            "Please enter Student ID and Name."
        )
        return

    lbl_prediction_val.config(text="Pass / High Score Expectation")
    lbl_risk_val.config(text="Low Risk")

    txt_recommendation.delete("1.0", tk.END)
    txt_recommendation.insert(
        tk.END,
        "Maintain current study patterns.\n"
        "Focus on consistency in internal assignments."
    )


def clear_fields():
    entry_student_id.delete(0, tk.END)
    entry_student_name.delete(0, tk.END)
    entry_attendance.delete(0, tk.END)
    entry_study_hours.delete(0, tk.END)
    entry_internal_marks.delete(0, tk.END)
    entry_assignment.delete(0, tk.END)
    entry_prev_score.delete(0, tk.END)

    lbl_prediction_val.config(text="_________")
    lbl_risk_val.config(text="_________")

    txt_recommendation.delete("1.0", tk.END)


def exit_program():
    root.destroy()

heading1 = tk.Label(
    root,
    text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1F4E78",
    fg="white",
    padx=20,
    pady=15
)

heading1.pack(fill="x")

container = tk.Frame(root, bg="#F2F2F2")
container.pack(fill="both", expand=True, padx=20, pady=20)

student_frame = tk.Frame(
    container,
    bg="white",
    bd=2,
    relief="groove"
)

student_frame.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="nsew"
)


heading2 = tk.Label(
    student_frame,
    text="Student Information",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1F4E78"
)

heading2.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=15
)

tk.Label(
    student_frame,
    text="Student ID:",
    bg="white"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

entry_student_id = tk.Entry(
    student_frame,
    width=25
)

entry_student_id.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    student_frame,
    text="Name:",
    bg="white"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

entry_student_name = tk.Entry(
    student_frame,
    width=25
)

entry_student_name.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)

academic_frame = tk.Frame(
    container,
    bg="white",
    bd=2,
    relief="groove"
)

academic_frame.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky="nsew"
)


heading3 = tk.Label(
    academic_frame,
    text="Academic Information",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1F4E78"
)

heading3.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=15
)

tk.Label(
    academic_frame,
    text="Attendance (%):",
    bg="white"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

entry_attendance = tk.Entry(
    academic_frame,
    width=25
)

entry_attendance.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)
tk.Label(
    academic_frame,
    text="Study Hours (per day):",
    bg="white"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

entry_study_hours = tk.Entry(
    academic_frame,
    width=25
)

entry_study_hours.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


tk.Label(
    academic_frame,
    text="Internal Marks (%):",
    bg="white"
).grid(row=3, column=0, padx=10, pady=8, sticky="w")

entry_internal_marks = tk.Entry(
    academic_frame,
    width=25
)

entry_internal_marks.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)


tk.Label(
    academic_frame,
    text="Assignment Completion (%):",
    bg="white"
).grid(row=4, column=0, padx=10, pady=8, sticky="w")

entry_assignment = tk.Entry(
    academic_frame,
    width=25
)

entry_assignment.grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    academic_frame,
    text="Previous Performance (%):",
    bg="white"
).grid(row=5, column=0, padx=10, pady=8, sticky="w")

entry_prev_score = tk.Entry(
    academic_frame,
    width=25
)

entry_prev_score.grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)

button_frame = tk.Frame(
    root,
    bg="#F2F2F2"
)

button_frame.pack(pady=10)
predict_btn = tk.Button(
    button_frame,
    text="Predict Performance",
    command=predict_performance,
    fg="blue",
    width=20
)

predict_btn.grid(
    row=0,
    column=0,
    padx=10
)


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    fg="green",
    width=12
)

clear_btn.grid(
    row=0,
    column=1,
    padx=10
)


exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=exit_program,
    fg="red",
    width=12
)

exit_btn.grid(
    row=0,
    column=2,
    padx=10
)

result_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

result_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


result_heading = tk.Label(
    result_frame,
    text="Predicted Result",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1F4E78"
)

result_heading.pack(pady=10)

lbl_prediction = tk.Label(
    result_frame,
    text="Prediction:",
    font=("Arial", 12, "bold"),
    bg="white"
)

lbl_prediction.pack(anchor="w", padx=20)


lbl_prediction_val = tk.Label(
    result_frame,
    text="_________",
    font=("Arial", 12),
    bg="white"
)

lbl_prediction_val.pack(anchor="w", padx=120)

lbl_risk = tk.Label(
    result_frame,
    text="Risk Level:",
    font=("Arial", 12, "bold"),
    bg="white"
)

lbl_risk.pack(anchor="w", padx=20, pady=(10, 0))


lbl_risk_val = tk.Label(
    result_frame,
    text="_________",
    font=("Arial", 12),
    bg="white"
)

lbl_risk_val.pack(anchor="w", padx=120)

lbl_recommendation = tk.Label(
    result_frame,
    text="Recommendation:",
    font=("Arial", 12, "bold"),
    bg="white"
)

lbl_recommendation.pack(anchor="w", padx=20, pady=(10, 0))


txt_recommendation = tk.Text(
    result_frame,
    height=3,
    width=70
)
txt_recommendation.pack(
    padx=20,
    pady=10
)

root.mainloop()