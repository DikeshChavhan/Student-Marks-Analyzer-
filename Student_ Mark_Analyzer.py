import streamlit as st
import pandas as pd

# Title of the app
st.title("🎓 Student Marks Analyzer")

# Sidebar for input
st.sidebar.header("Enter Student Data")

# Taking input
name = st.sidebar.text_input("Student Name")
marks = st.sidebar.slider("Marks (out of 100)", 0, 100, 50)

# Store data
if "students" not in st.session_state:
    st.session_state["students"] = []

if st.sidebar.button("Add Student"):
    st.session_state["students"].append({"Name": name, "Marks": marks})
    st.sidebar.success(f"{name} added!")

# Display table
if st.session_state["students"]:
    df = pd.DataFrame(st.session_state["students"])
    st.subheader("📋 Student Records")
    st.dataframe(df)

    # Show statistics
    avg = df["Marks"].mean()
    st.metric("Average Marks", f"{avg:.2f}")

    # Chart
    st.bar_chart(df.set_index("Name"))
