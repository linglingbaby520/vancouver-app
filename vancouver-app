import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Welcome to Vancouver 🇨🇦")
st.write("An incredible view of the city and mountains.")

# We need to load the image. Streamlit can load images from a local file
# OR from a web URL. Since I just generated this image, I'll use its web address.
image_url = "https://replicate.delivery/xpbkg/d8aL6f9q9f0xR6Y5E7w8Y3N2E1c9q6V8A0V2N5E6A7a9V6YQA/out-0.png"

try:
    # This fetches the image data from the internet
    response = requests.get(image_url)
    # This opens the image data so Python can understand it
    img = Image.open(BytesIO(response.content))
    # This displays the image on your Streamlit app
    st.image(img, caption="Vancouver, BC at Sunset")
except Exception as e:
    st.error(f"Could not load the image. Error: {e}")

st.write("This is just the start! What else do you want to put on this page?")
