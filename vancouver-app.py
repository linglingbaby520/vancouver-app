import streamlit as st

st.title("Welcome to Vancouver 🇨🇦")
st.write("An incredible view of the city and mountains.")

# Using a stable public image link for Vancouver
image_url = "https://images.unsplash.com/photo-1559563458-527698bf5295?auto=format&fit=crop&w=1200&q=80"

st.image(image_url, caption="Vancouver, BC skyline")

st.write("This is just the start! What else do you want to put on this page?")
