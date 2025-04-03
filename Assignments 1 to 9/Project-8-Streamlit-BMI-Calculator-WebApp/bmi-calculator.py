import streamlit as st

# Title
st.title("💪 BMI Calculator")

# Input Fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)

        # BMI Categories
        if bmi < 18.5:
            category = "Underweight"
            color = "🔵"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "🟢"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "🟠"
        else:
            category = "Obese"
            color = "🔴"

        # Display Results
        st.success(f"Your BMI is **{bmi:.2f}**")
        st.markdown(f"### {color} Category: **{category}**")
    else:
        st.error("Please enter valid weight and height!")

