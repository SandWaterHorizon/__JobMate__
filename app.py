# app.py #

import os
import time
import json
from threading import Thread
from dotenv import load_dotenv
from flask import Flask
from twilio.rest import Client

import incoming_msg

# Load environment variables from .env file
load_dotenv()

ACCOUNT_SID = os.getenv("MS_TWILIO_ACCOUNT_SID")
API_KEY_SID = os.getenv("MS_TWILIO_API_KEY_SID")
API_KEY_SECRET = os.getenv("MS_TWILIO_SECRET")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
MS_NUMBER = os.getenv("MS_NUMBER")
SERVICE_SID = os.getenv("MS_TWILIO_DEFAULT_SERVICE_SID")

# Normalize WhatsApp phone numbers
PHONE_NUMBER = f"whatsapp:{PHONE_NUMBER.replace('whatsapp:', '').strip()}"
MS_NUMBER = f"whatsapp:{MS_NUMBER.replace('whatsapp:', '').strip()}"


# Initialize Twilio client and service
client = Client(API_KEY_SID, API_KEY_SECRET, ACCOUNT_SID)
service = client.conversations.v1.services(SERVICE_SID)


# STEP 1: Send initial WhatsApp message using Messaging API
message = client.messages.create(
    body=(
        "👋 Welcome to *JobMate*!\n\n"
        "Let's find your dream job together.\n\n"
                
        "🔍 How it works: \n"
        "• We search for jobs across top platforms like Glassdoor, LinkedIn, Indeed, and StepStone.\n"
        "• You’ll get refined and personalized results based on your search.\n"
        "You can save the results.\n"
        
        "🧭 Just type in a job title and the city you’re interested in —\n"
        "(e.g., “frontend developer in Berlin”)"
    ),
    from_=MS_NUMBER,
    to=PHONE_NUMBER
)


print("from server (Messaging API):", message.body)
print("✅ Message SID:", message.sid)

# STEP 2: Reuse or create a conversation
existing_conversations = service.conversations.list()
conversation = next((c for c in existing_conversations if c.friendly_name == 'Friendly Conversation'), None)

if conversation:
    print("ℹ️ Reusing existing conversation.")
else:
    conversation = service.conversations.create(friendly_name='Friendly Conversation')
    print("✅ Created new conversation.")


# Check if the participant is already in the conversation
participants = conversation.participants.list()
already_added = any(p.messaging_binding['address'] == PHONE_NUMBER for p in participants)


if not already_added:
    print(f"Adding participant with address: {PHONE_NUMBER}")
    print(f"Using proxy address: {MS_NUMBER}")
    conversation.participants.create(
        messaging_binding_address=PHONE_NUMBER,
        messaging_binding_proxy_address=MS_NUMBER
    )
    print("✅ Participant added to conversation.")
else:
    print("ℹ️ Participant already exists in the conversation.")

# Flask app is optional here, only to show server is running
app = Flask(__name__)

@app.route("/")
def index():
    return "🚀 Flask is running!"

if __name__ == "__main__":
    Thread(target=lambda: app.run(port=8080)).start()
    print("📲 Waiting for replies from your WhatsApp...")
    last_sid = None

    while True:
        messages = conversation.messages.list()
        if messages:
            last_msg = messages[-1]

            if last_msg.sid != last_sid and last_msg.author == PHONE_NUMBER:
                print("from phone:", last_msg.body)

                reply = incoming_msg.handle_incoming_message(last_msg.body)

                incoming_msg.handle_incoming_message("help")

                print("from server:", reply)
                conversation.messages.create(author="system", body=reply)
                last_sid = last_msg.sid


        time.sleep(1)


# app.py #