import streamlit as st

st.title("📢 BC & Vancouver News Hub")
st.write("Your quick directory for local media channels, TV news, newspapers, and digital outlets.")

# List of media channels with categories, images, and links
media_channels = [
    {
        "name": "CTV News Vancouver",
        "type": "TV / Broadcast",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/CTV_News_Channel_%28Canada%29_logo.svg/250px-CTV_News_Channel_%28Canada%29_logo.svg.png",
        "url": "https://bc.ctvnews.ca/"
    },
    {
        "name": "Richmond News",
        "type": "Newspaper",
        "image": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?auto=format&fit=crop&w=600&q=80",
        "url": "https://www.richmond-news.com/"
    },
    {
        "name": "604 Now",
        "type": "Digital Media",
        "image": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=600&q=80",
        "url": "https://604now.com/"
    },
    {
        "name": "Global News BC",
        "type": "TV / YouTube",
        "image": "https://images.unsplash.com/photo-1495020689067-958ab52e3367?auto=format&fit=crop&w=600&q=80",
        "url": "https://globalnews.ca/bc/"
    }
]

# Display channels in an organized layout
for channel in media_channels:
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(channel["image"], width=180)
            
        with col2:
            st.subheader(channel["name"])
            st.markdown(f"**Category:** {channel['type']}")
            st.markdown(f"[Visit Website / Feed]({channel['url']})")
            
        st.divider()
