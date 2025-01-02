import streamlit as st 
import pandas as pd

if 'students' not in st.session_state:
        st.session_state.students = []
        
name = st.text_input("Student Name", placeholder="Enter student name")
score = st.number_input("Score (0-100)", min_value=0, max_value=100, step=1, value=0)
if st.button("Add Student"):
      
    if name: 
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f"Added: {name} with Score: {score}")
    else:
        st.error("Please enter a valid name.")
        
st.subheader("Student Data")
if st.session_state.students:
    student_df = pd.DataFrame(st.session_state.students)
    st.write(student_df)
else:
    st.info("No students have been added yet.")
    
st.subheader("Filter by Minimum Score")
min_score = st.slider("Minimum Score", min_value=0, max_value=100, value=50)
filtered_students = (
    pd.DataFrame(st.session_state.students)
    if st.session_state.students
    else pd.DataFrame(columns=["Name", "Score"])
)
filtered_students = filtered_students[filtered_students["Score"] >= min_score]

st.write(f"Students with scores >= {min_score}:")
st.write(filtered_students)