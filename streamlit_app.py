import streamlit as st
import joblib

model = joblib.load("model (1).pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("SMS Spam Detector")
text = st.text_area("Enter SMS message")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a message.")
    else:
        pred = model.predict(vectorizer.transform([text]))[0]
        if pred == 1:
            st.error("Spam")
        else:
            st.success("Not Spam (Ham)")
