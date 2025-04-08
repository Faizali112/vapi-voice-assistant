from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔑 Replace this with your actual API key or load from environment variables
openai.api_key = "sk-Y2xqlD1kP76MlfLeaYajhtQ6SZl2Ra1JYpdPsJSxk3WbbgnV"

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_google_meet(summary="Voice Assistant Meet", start_time=None, duration_minutes=30):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    if not start_time:
        start_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    end_time = start_time + datetime.timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat() + 'Z'},
        'end': {'dateTime': end_time.isoformat() + 'Z'},
        'conferenceData': {
            'createRequest': {
                'requestId': 'voice-assistant-meeting',
                'conferenceSolutionKey': {'type': 'hangoutsMeet'},
            }
        }
    }

    created_event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    return created_event['hangoutLink']


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get("message", "")

    print("User said:", user_message)

    if "meet" in user_message.lower():
        try:
            meet_link = create_google_meet()
            reply = f"Here is your Google Meet link: {meet_link}"
        except Exception as e:
            print("Error creating meeting:", e)
            reply = "I couldn't create a meeting right now."
    else:
        # fallback to OpenAI
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = completion.choices[0].message['content'].strip()

    return jsonify({"response": reply})


if __name__ == '__main__':
    app.run(port=3000)
