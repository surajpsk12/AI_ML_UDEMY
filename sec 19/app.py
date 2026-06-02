import streamlit as st


st.set_page_config(page_title="Student Form", page_icon="🎓", layout="wide")

st.title("Student Information Form")
st.caption("Fill in the student details, marks, and result information below.")


with st.form("student_form"):
	st.subheader("Basic Details")
	left_col, right_col = st.columns(2)

	with left_col:
		student_name = st.text_input("Student Name")
		father_name = st.text_input("Father Name")
		roll_number = st.text_input("Roll Number")
		class_name = st.text_input("Class")
		section = st.text_input("Section")

	with right_col:
		age = st.number_input("Age", min_value=1, max_value=100, value=18, step=1)
		gender = st.selectbox("Gender", ["Male", "Female", "Other"])
		school_name = st.text_input("School Name")
		academic_year = st.text_input("Academic Year", value="2025-2026")

	st.subheader("Subjects and Marks")
	marks_col1, marks_col2, marks_col3 = st.columns(3)

	with marks_col1:
		english = st.number_input("English Marks", min_value=0, max_value=100, value=0, step=1)
		math = st.number_input("Math Marks", min_value=0, max_value=100, value=0, step=1)

	with marks_col2:
		science = st.number_input("Science Marks", min_value=0, max_value=100, value=0, step=1)
		social = st.number_input("Social Studies Marks", min_value=0, max_value=100, value=0, step=1)

	with marks_col3:
		computer = st.number_input("Computer Marks", min_value=0, max_value=100, value=0, step=1)
		additional_subject = st.text_input("Additional Subject", value="")
		additional_marks = st.number_input("Additional Subject Marks", min_value=0, max_value=100, value=0, step=1)

	remarks = st.text_area("Remarks")
	submitted = st.form_submit_button("Submit Student Form")


if submitted:
	subject_marks = {
		"English": english,
		"Math": math,
		"Science": science,
		"Social Studies": social,
		"Computer": computer,
	}

	if additional_subject.strip():
		subject_marks[additional_subject.strip()] = additional_marks

	marks_rows = [{"Subject": subject, "Marks": marks} for subject, marks in subject_marks.items()]

	total_marks = int(sum(subject_marks.values()))
	max_marks = len(marks_rows) * 100
	percentage = round((total_marks / max_marks) * 100, 2) if max_marks else 0
	result = "Pass" if all(mark >= 35 for mark in subject_marks.values()) else "Fail"

	st.success("Student form submitted successfully.")

	info_col1, info_col2 = st.columns(2)
	with info_col1:
		st.subheader("Student Details")
		st.write(f"**Name:** {student_name}")
		st.write(f"**Father Name:** {father_name}")
		st.write(f"**Roll Number:** {roll_number}")
		st.write(f"**Class:** {class_name}")
		st.write(f"**Section:** {section}")

	with info_col2:
		st.subheader("Academic Details")
		st.write(f"**Age:** {age}")
		st.write(f"**Gender:** {gender}")
		st.write(f"**School Name:** {school_name}")
		st.write(f"**Academic Year:** {academic_year}")

	st.subheader("Marks Summary")
	st.table(marks_rows)

	summary_col1, summary_col2, summary_col3 = st.columns(3)
	summary_col1.metric("Total Marks", total_marks)
	summary_col2.metric("Percentage", f"{percentage}%")
	summary_col3.metric("Result", result)

	st.subheader("Remarks")
	st.write(remarks if remarks.strip() else "No remarks provided.")
