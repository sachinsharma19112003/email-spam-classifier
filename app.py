import streamlit as st
import pickle

# Load model & vectorizer
with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Page Title
st.title("📩 SMS Spam Classifier")
st.write("Enter a message below to check whether it is Spam or Ham.")

# User Input
message = st.text_area("Enter your message:")

if st.button("Predict"):

    if message.strip() != "":
        message_tfidf = vectorizer.transform([message])
        prediction = model.predict(message_tfidf)

        if prediction[0] == 1:
            st.error("🚨 This is a Spam Message")
        else:
            st.success("✅ This is a Ham Message")
    else:
        st.warning("Please enter a message first.")