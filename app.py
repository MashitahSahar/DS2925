import streamlit as st

# Title of the app
st.title("Finance Data")


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
