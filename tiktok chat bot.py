import json
import requests

# Set your TikTok API key
API_KEY = "YOUR_API_KEY"

# Get the live chat stream ID
LIVE_CHAT_STREAM_ID = "YOUR_LIVE_CHAT_STREAM_ID"

# Create a list of blocked words
BLOCKED_WORDS = ["badword1", "badword2", "badword3"]

# Define a function to moderate the chat
def moderate_chat(chat_message):
    # Check if the chat message contains a blocked word
    for blocked_word in BLOCKED_WORDS:
        if blocked_word in chat_message:
            return True

    return False

# Start a loop to monitor the chat stream
while True:
    # Get the latest chat messages
    response = requests.get(f"https://api.tiktok.com/tiktok/chat/messages?stream_id={LIVE_CHAT_STREAM_ID}&api_key={API_KEY}")

    # Parse the JSON response
    chat_messages = json.loads(response.content)["messages"]

    # Iterate over the chat messages and moderate them
    for chat_message in chat_messages:
        # Check if the chat message contains a blocked word
        if moderate_chat(chat_message["message"]):
            # Delete the chat message
            requests.delete(f"https://api.tiktok.com/tiktok/chat/messages/{chat_message['id']}?api_key={API_KEY}")

