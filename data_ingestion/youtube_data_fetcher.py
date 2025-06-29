import requests
import json

# Replace with your actual API key
API_KEY = "YOUR_YOUTUBE_API_KEY"
CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Example: Google Developers Channel

# Build URL
url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=10"

# Make the request
response = requests.get(url)
data = response.json()

# Print video titles
for item in data['items']:
    title = item['snippet']['title']
    published = item['snippet']['publishedAt']
    print(f"Title: {title} | Published: {published}")
