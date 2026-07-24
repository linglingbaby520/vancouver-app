import streamlit as st

st.title("Vancouver Explorer 🇨🇦")
st.write("Click the button to explore different iconic views of the city!")

# A list of stunning Vancouver image links
vancouver_images = [
    {
        "url": "https://images.unsplash.com/photo-1559563458-527698bf5295?auto=format&fit=crop&w=1200&q=80",
        "caption": "Vancouver Skyline and North Shore Mountains"
    },
    {
        "url": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=1200&q=80",
        "caption": "Gastown Steam Clock Area"
    },
    {
        "url": "https://images.unsplash.com/photo-1507035895480-2b3156c31fc8?auto=format&fit=crop&w=1200&q=80",
        "caption": "Lions Gate Bridge and Stanley Park"
    }
]

# Track which image we are looking at in session state
if "img_index" not in st.session_state:
    st.session_state.img_index = 0

# Button to cycle to the next image
if st.button("Show Another View 📸"):
    st.session_state.img_index = (st.session_state.img_index + 1) % len(vancouver_images)

# Get the current image details
current_image = vancouver_images[st.session_state.img_index]

# Display the image and caption
st.image(current_image["url"], caption=current_image["caption"])
