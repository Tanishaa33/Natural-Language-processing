import streamlit as st
import pickle

# Load trained model
with open("trained_model.sav", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 Sentiment Analysis")
st.write("Enter a review or sentence and the model will predict its sentiment.")

# Text input
text = st.text_area(
    "Enter your text:",
    placeholder="Example: I really loved this movie!"
)

# Predict button
if st.button("Predict Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([text])[0]

        # Adjust these labels according to your model
        if prediction == 1:
            st.success("😊 Positive Sentiment")
        else:
            st.error("😞 Negative Sentiment")
