import streamlit as st

st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 World Cities Explorer")

# Welcome text
st.markdown("""
    Welcome to the World Cities Explorer! This app provides information and insights about cities around the world.
    
    Use the sidebar to navigate to different sections of the app.
""")

# Button to navigate to app
if st.button("Go to App →", use_container_width=True, type="primary"):
    st.switch_page("pages/app.py")

st.divider()

# Optional: Add some footer content
st.markdown("""
    ---
    ### How to use this app
    - Navigate using the sidebar pages
    - Explore city data and visualizations
    - Discover interesting facts about world cities
""")
