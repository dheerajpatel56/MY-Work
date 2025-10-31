import os
import datetime
import pytz
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------
# 1️⃣ Load Environment Variables
# -----------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------
# 2️⃣ Configuration
# -----------------------
SPREADSHEET_ID = "1g97KhVbGMoRtJCkh-ZXz3n21-XYCK8W4RLZ9IlYhuX4"
RANGE_NAME = "'Faculty Timetable'!A2:I"


TIMEZONE = pytz.timezone("Asia/Kolkata")

# -----------------------
# 3️⃣ Initialize Gemini
# -----------------------
genai.configure(api_key=GEMINI_API_KEY)

def generate_formal_reminder(faculty, subject, class_name, room, start_time):
    prompt = f"""
    Write a short, formal academic email reminder to {faculty}, 
    informing them that their class on {subject} for {class_name} 
    is scheduled to begin at {start_time} in {room}. 
    Use a professional and polite tone.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# -----------------------
# 4️⃣ Google Sheets Setup (Service Account)
# -----------------------
def get_sheet_data():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = service_account.Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    return result.get("values", [])

# -----------------------
# 5️⃣ Gmail OAuth Setup
# -----------------------
def get_gmail_service():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    if os.path.exists("token_gmail.pickle"):
        with open("token_gmail.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "gmail_credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token_gmail.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("gmail", "v1", credentials=creds)

# -----------------------
# 6️⃣ Send Gmail Function
# -----------------------
def send_email(service, to, subject, message_text):
    message = MIMEText(message_text)
    message["to"] = to
    message["subject"] = subject
    raw = urlsafe_b64encode(message.as_bytes()).decode()
    body = {"raw": raw}
    service.users().messages().send(userId="me", body=body).execute()
    print(f"📧 Sent reminder to: {to}")

# -----------------------
# 7️⃣ Main Reminder Logic
# -----------------------
def main():
    print("📅 Fetching timetable...")
    rows = get_sheet_data()
    gmail_service = get_gmail_service()

    now = datetime.datetime.now(TIMEZONE)
    upcoming = []

    for row in rows:
        try:
            faculty, email, subject, class_name, start_time, end_time, room, status, notes = (row + [""] * 9)[:9]
            if not start_time or status.lower() == "done":
                continue

            start_dt = datetime.datetime.fromisoformat(start_time).astimezone(TIMEZONE)
            diff = (start_dt - now).total_seconds() / 60  # difference in minutes

            if 0 <= diff <= 5:  # within 5 minutes
                upcoming.append({
                    "faculty": faculty,
                    "email": email,
                    "subject": subject,
                    "class": class_name,
                    "start_time": start_dt.strftime("%H:%M"),
                    "room": room
                })
        except Exception as e:
            print("⚠️ Error parsing row:", row, e)

    if not upcoming:
        print("✅ No upcoming classes within 5 minutes.")
        return

    for event in upcoming:
        reminder = generate_formal_reminder(
            event["faculty"], event["subject"], event["class"], event["room"], event["start_time"]
        )
        send_email(
            gmail_service,
            event["email"],
            f"Reminder: {event['subject']} Class at {event['start_time']}",
            reminder,
        )

    print("🎯 All reminders sent successfully!")

# -----------------------
# 8️⃣ Run the Bot
# -----------------------
if __name__ == "__main__":
    main()
