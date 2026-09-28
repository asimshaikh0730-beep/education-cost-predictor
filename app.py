import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Education Cost Predictor")

df = pd.read_csv("International_Education_Costs.csv")
model = pickle.load(open("model.pkl", "rb"))

# LabelEncoder alphabetical order mein number deta hai, wahi yahan bana rahe hain
cat_cols = ["Country", "City", "University", "Program", "Level"]
maps = {
    c: {v: i for i, v in enumerate(sorted(df[c].astype(str).unique()))}
    for c in cat_cols
}

st.title("🎓 International Education Cost Predictor")

country = st.selectbox("Country", sorted(maps["Country"]))
city = st.selectbox("City", sorted(maps["City"]))
university = st.selectbox("University", sorted(maps["University"]))
program = st.selectbox("Program", sorted(maps["Program"]))
level = st.selectbox("Level", sorted(maps["Level"]))
duration = st.number_input("Duration (Years)", 0.5, 6.0, 2.0, step=0.5)
living = st.number_input("Living Cost Index", 0.0, 200.0, 75.0)
visa = st.number_input("Visa Fee (USD)", 0, 2000, 200)
insurance = st.number_input("Insurance (USD)", 0, 5000, 800)

if st.button("Predict Total Cost"):
    X = pd.DataFrame([[
        maps["Country"][country],
        maps["City"][city],
        maps["University"][university],
        maps["Program"][program],
        maps["Level"][level],
        duration, living, visa, insurance,
    ]], columns=["Country", "City", "University", "Program", "Level",
                 "Duration_Years", "Living_Cost_Index",
                 "Visa_Fee_USD", "Insurance_USD"])
    pred = model.predict(X)[0]
    st.success(f"Estimated Total Cost: ${pred:,.0f}")