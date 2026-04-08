import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# -----------------------------
# DATABASE SETUP
# -----------------------------
conn = sqlite3.connect("clinic.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    disease TEXT,
    symptom TEXT,
    date TEXT
)
""")
conn.commit()

# -----------------------------
# UI TITLE
# -----------------------------
st.title("🏥 Clinic Disease Analysis System")

# -----------------------------
# USER INPUT FORM
# -----------------------------
st.header("➕ Add Patient Data")

name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 100)
disease = st.text_input("Disease")
symptom = st.text_input("Symptom")
date = st.date_input("Visit Date")

if st.button("Add Record"):
    cursor.execute(
        "INSERT INTO patients (name, age, disease, symptom, date) VALUES (?, ?, ?, ?, ?)",
        (name, age, disease, symptom, str(date))
    )
    conn.commit()
    st.success("✅ Record Added!")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_sql_query("SELECT * FROM patients", conn)

if not df.empty:
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month

    st.header("📊 Data Overview")
    st.dataframe(df)

    # -----------------------------
    # COMMON DISEASES
    # -----------------------------
    st.subheader("📌 Most Common Diseases")
    disease_count = df["disease"].value_counts()
    st.write(disease_count)

    # -----------------------------
    # COMMON SYMPTOMS
    # -----------------------------
    st.subheader("🩺 Most Common Symptoms")
    symptom_count = df["symptom"].value_counts()
    st.write(symptom_count)

    # -----------------------------
    # SEASONAL ANALYSIS
    # -----------------------------
    st.subheader("📅 Monthly Cases Trend")

    monthly = df.groupby("month")["disease"].count()

    fig, ax = plt.subplots()
    monthly.plot(kind="bar", ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Cases")
    ax.set_title("Cases Per Month")

    st.pyplot(fig)

    # -----------------------------
    # INSIGHTS
    # -----------------------------
    st.subheader("💡 Insights")

    st.write(f"Most common disease: {disease_count.idxmax()}")
    st.write(f"Most common symptom: {symptom_count.idxmax()}")
    st.write("Prepare medicines and staff based on trends.")
else:
    st.warning("⚠️ No data available. Please add records.")