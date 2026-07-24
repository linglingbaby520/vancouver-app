import streamlit as st

st.title("📢 BC & Vancouver News Hub")
st.write("Local media channels, TV news, newspapers, and digital outlets.")

st.markdown("---")

# Dictionary or list of categories and links
news_links = [
    {"name": "CTV News Vancouver", "type": "TV", "url": "https://bc.ctvnews.ca/"},
    {"name": "Richmond News", "type": "Newspaper", "url": "https://www.richmond-news.com/"},
    {"name": "604 Now", "type": "Digital", "url": "https://604now.com/"},
    {"name": "Global News BC", "type": "TV / YouTube", "url": "https://globalnews.ca/bc/"},
    {"name": "CBC News British Columbia", "type": "TV / Digital", "url": "https://www.cbc.ca/news/canada/british-columbia"},
    {"name": "Vancouver Sun", "type": "Newspaper", "url": "https://vancouversun.com/"},
    {"name": "Daily Hive Vancouver", "type": "Digital", "url": "https://dailyhive.com/vancouver"}
]

# Display in a clean, text-heavy layout
for item in news_links:
    st.markdown(f"**[{item['name']}]({item['url']})** — *{item['type']}*")

st.markdown("---")
st.write("*(July 2026)*")
