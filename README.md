# 🎓 Student Recruitment Management System

A desktop-based **Student Recruitment Management System** built using Python and Tkinter.
This application helps manage student records and allows recruiters to filter candidates based on eligibility criteria such as CGPA, experience, backlogs, and relocation preference.

---

##  Project Overview

This system provides a simple and user-friendly graphical interface to:

* Add student details
* View all stored student records
* Filter students based on recruiter requirements
* Validate input data to maintain accuracy

The application stores data temporarily using Python lists and displays records using Pandas DataFrame format.

---

##  Features

###  Add Student

* Stores student details including academic and personal information
* Performs input validation
* Converts numeric values safely (Age, CGPA, Experience, Backlogs)

###  View Students

* Displays all student records
* Uses Pandas to show structured tabular format

###  Filter Students

Recruiters can filter candidates based on:

* Minimum CGPA
* Minimum Experience (Years)
* Maximum Backlogs
* Willingness to Relocate

If no students match the criteria, an appropriate message is displayed.

---

##  Technologies Used

* **Python**
* **Tkinter** (GUI Framework)
* **Pandas** (Data handling and tabular display)

---

##  System Architecture

The application follows a modular structure:

* **GUI Layer** – Built using Tkinter for user interaction
* **Logic Layer** – Handles student addition, filtering, and validation
* **Data Layer** – Stores student data using Python list of dictionaries

All modules work together inside a single Python file.

---

##  Data Structure

Student data is stored in the following dictionary format:

```python
{
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
}
```

All student records are appended to a list called:

```python
students = []
```

---

##  Filtering Logic

Students are filtered using the following conditions:

```python
s["CGPA"] >= min_cgpa
s["Experience (Years)"] >= min_exp
s["Backlogs"] <= max_backlogs
```

Relocation condition:

* If recruiter selects "Yes", all students are considered.
* If recruiter selects "No", only students unwilling to relocate are filtered accordingly.

---

##  Input Validation & Error Handling

The system ensures:

* All fields must be filled.
* Age, CGPA, Experience, and Backlogs must be numeric.
* Error messages are displayed for invalid inputs.
* ValueError is handled gracefully.

---

##  How to Run the Project

### Step 1: Install Requirements

Make sure Python is installed.

Install Pandas (if not already installed):

```bash
pip install pandas
```

### Step 2: Run the Application

```bash
python filename.py
```

The GUI window will open.

---

##  Application Interface

The interface contains:

* Input fields for student details
* Dropdown menu for relocation preference
* Buttons:

  * Add Student
  * View Students
  * Filter Students
* Recruiter filter section

---

##  Advantages

* Easy-to-use GUI
* Structured student data storage
* Efficient filtering mechanism
* Error handling and validation
* Suitable for small-scale recruitment management

---

##  Limitations

* Data is stored temporarily (no database)
* Single-user desktop application
* No authentication system
* Not scalable for large datasets

---

##  Future Enhancements

* Add database integration (MySQL / SQLite)
* Implement login authentication
* Export filtered data to Excel or PDF
* Convert to web-based application
* Improve UI design and styling

---

##  Learning Outcomes

This project demonstrates:

* GUI development using Tkinter
* Data manipulation using Pandas
* Input validation and error handling
* Implementation of filtering logic
* Modular Python programming

---

