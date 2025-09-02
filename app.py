import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}! 👋")
    st.write(f"You are {age} years old.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (from your GitHub raw CSV)
url = "https://raw.githubusercontent.com/MashitahSahar/DS2925/refs/heads/main/Finance_data.csv"
df = pd.read_csv(url)

# Title
st.title("Histogram of Age Distribution")

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='age', bins=10, kde=True, ax=ax)
ax.set_title('Histogram of Age Distribution')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

# Show in Streamlit
st.pyplot(fig)
