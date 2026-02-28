import tkinter as tk
from tkinter import messagebox
import pandas as pd

# -------------------- Data Storage --------------------
students = []

# -------------------- Functions --------------------

def add_student():
    try:
        name = student_name_entry.get()
        age = student_age_entry.get()
        major = student_major_entry.get()
        languages = student_languages_entry.get()
        experience = student_experience_entry.get()
        cgpa = student_cgpa_entry.get()
        relocate = relocate_var.get()
        backlogs = student_backlogs_entry.get()
        phone = student_phone_entry.get()
        email = student_email_entry.get()
        certifications = student_certifications_entry.get()

        # Validate required fields
        if not all([name, age, major, languages, experience, cgpa,
                    backlogs, phone, email, certifications]):
            messagebox.showerror("Input Error", "Please fill all fields.")
            return

        # Store student data
        students.append({
            "Name": name,
            "Age": int(age),
            "Major": major,
            "Languages Known": languages,
            "Experience (Years)": float(experience),
            "CGPA": float(cgpa),
            "Willing to Relocate": relocate,
            "Backlogs": int(backlogs),
            "Phone Number": phone,
            "Email ID": email,
            "Certifications": certifications
        })

        clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


def view_students():
    if not students:
        messagebox.showinfo("Info", "No students available.")
        return

    df = pd.DataFrame(students)
    messagebox.showinfo("Students", df.to_string(index=False))


def filter_students():
    if not students:
        messagebox.showinfo("Info", "No students available.")
        return

    try:
        min_cgpa = float(min_cgpa_entry.get())
        min_exp = float(min_experience_entry.get())
        max_backlogs = int(max_backlogs_entry.get())
        relocate_pref = relocate_filter_var.get()

        filtered = [
            s for s in students
            if s["CGPA"] >= min_cgpa
            and s["Experience (Years)"] >= min_exp
            and s["Backlogs"] <= max_backlogs
            and (relocate_pref == "Yes" or s["Willing to Relocate"] == "No")
        ]

        if filtered:
            df = pd.DataFrame(filtered)
            messagebox.showinfo("Filtered Students", df.to_string(index=False))
        else:
            messagebox.showinfo("Result", "No students match the criteria.")

    except ValueError:
        messagebox.showerror("Input Error", "Invalid filter values.")


def clear_fields():
    entries = [
        student_name_entry,
        student_age_entry,
        student_major_entry,
        student_languages_entry,
        student_experience_entry,
        student_cgpa_entry,
        student_backlogs_entry,
        student_phone_entry,
        student_email_entry,
        student_certifications_entry
    ]

    for entry in entries:
        entry.delete(0, tk.END)

    relocate_var.set("No")


# -------------------- GUI Setup --------------------

root = tk.Tk()
root.title("Student Recruitment Management System")
root.geometry("500x750")

tk.Label(root,
         text="Student Recruitment Management System",
         font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

labels = [
    "Name",
    "Age",
    "Major",
    "Languages Known",
    "Experience (Years)",
    "CGPA",
    "Backlogs",
    "Phone Number",
    "Email ID",
    "Certifications"
]

entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label + ":").grid(row=i + 1, column=0,
                                          sticky=tk.W, padx=10, pady=5)
    entry = tk.Entry(root, width=30)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    entries.append(entry)

(
    student_name_entry,
    student_age_entry,
    student_major_entry,
    student_languages_entry,
    student_experience_entry,
    student_cgpa_entry,
    student_backlogs_entry,
    student_phone_entry,
    student_email_entry,
    student_certifications_entry
) = entries

# Relocation Dropdown
tk.Label(root, text="Willing to Relocate:").grid(row=11, column=0,
                                                 sticky=tk.W, padx=10)
relocate_var = tk.StringVar(value="No")
tk.OptionMenu(root, relocate_var, "Yes", "No").grid(row=11, column=1)

# Buttons
tk.Button(root, text="Add Student", width=20,
          command=add_student).grid(row=12, column=0, pady=10)

tk.Button(root, text="View Students", width=20,
          command=view_students).grid(row=12, column=1, pady=10)

# Divider
tk.Label(root, text="-" * 60).grid(row=13, column=0,
                                   columnspan=2, pady=10)

# Recruiter Filter Section
tk.Label(root, text="Recruiter Filters",
         font=("Arial", 14, "bold")).grid(row=14,
                                          column=0,
                                          columnspan=2,
                                          pady=10)

tk.Label(root, text="Minimum CGPA:").grid(row=15,
                                          column=0,
                                          sticky=tk.W,
                                          padx=10)
min_cgpa_entry = tk.Entry(root)
min_cgpa_entry.grid(row=15, column=1)

tk.Label(root, text="Minimum Experience (Years):").grid(row=16,
                                                        column=0,
                                                        sticky=tk.W,
                                                        padx=10)
min_experience_entry = tk.Entry(root)
min_experience_entry.grid(row=16, column=1)

tk.Label(root, text="Maximum Backlogs:").grid(row=17,
                                              column=0,
                                              sticky=tk.W,
                                              padx=10)
max_backlogs_entry = tk.Entry(root)
max_backlogs_entry.grid(row=17, column=1)

tk.Label(root, text="Willing to Relocate:").grid(row=18,
                                                 column=0,
                                                 sticky=tk.W,
                                                 padx=10)
relocate_filter_var = tk.StringVar(value="Yes")
tk.OptionMenu(root, relocate_filter_var, "Yes", "No").grid(row=18, column=1)

tk.Button(root,
          text="Filter Students",
          width=25,
          command=filter_students).grid(row=19,
                                        column=0,
                                        columnspan=2,
                                        pady=20)

root.mainloop()
