import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("housing.csv")

# Title
st.title("California Housing Data (1990) by Yuhan Dang")

# Slider
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

# Filter by house value
filtered_df = df[df["median_house_value"] >= min_value]

# Subheader
st.subheader("See more filters in the sidebar:")

# Sidebar: Location type
location_types = st.sidebar.multiselect(
    "Choose the location type",
    options=df["ocean_proximity"].unique(),
    default=df["ocean_proximity"].unique()
)

filtered_df = filtered_df[
    filtered_df["ocean_proximity"].isin(location_types)
]

# Sidebar: Income level
income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

if income_level == "Low":
    filtered_df = filtered_df[
        filtered_df["median_income"] <= 2.5
    ]

elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5) &
        (filtered_df["median_income"] < 4.5)
    ]

else:
    filtered_df = filtered_df[
        filtered_df["median_income"] >= 4.5
    ]

# Map
st.map(filtered_df)

# Histogram
st.subheader("Distribution of Median House Values")

fig, ax = plt.subplots()

ax.hist(
    filtered_df["median_house_value"],
    bins=30
)

ax.set_xlabel("Median House Value")
ax.set_ylabel("Frequency")

st.pyplot(fig)
