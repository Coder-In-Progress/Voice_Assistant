from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ['January', 'febuary', 'march', 'april', may', 'june', 'july', 'august', 'september', 'november', 'december']
DAYS = [monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
DAY_ABRE = ["rd", "th", "st", "nd"]

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "recording.mp3"
	tts.save(filename)
	playsound.playsound(filename)



def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
			audio = r.listen(source)
			said = ""

			try:
				said = r.recognize_google(audio)
				print(said)
			except Esception as e:
				print("Exception: " + str(e))
	return said


speak ("Hello Jithesh")
get_audio()

text = get_audio()

if "hello" in text:
	speak("hello")
	
if "what is your favorite color" in text:
	speak("red")
	
if "who is the greatest person in the entire universe" in text:
	speak("Jithesh")
	
if "what is your name" in text:
	speak("Jbob!")
	
def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

	return service
def get_events(day, service)
    # Call the Calendar API
	date = datetime.datetime.combine(day, datetime.datetime.min.time())
	end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
	utc = pytz.EST
	date = date.astimezone(est)
	end_date = end_date.astimezone(est)
	
    
 	events_result = service.events().list(calendarID='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat()                              
				       	singleEvents=True,
                                        orderBy='startTime').execute()
 events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def get_date(text
	text=text.lower()
	today = datetime.date.today()
	
	if text.count ("today") > 0:
		return today
		
	day = -1
	day_of_week = -1
	month = -1
	year = today.year
	
	for word in text.split()
		if word in months:
			month = MONTHS.index(month) + 1
		elif word in months:
			days_of_week = DAYS.index(word)
		elif word.isdigit():
			day = int(word)
		else:
			for ext in DAY_ABRE:
			found = word.find(ext)
			if found > 0:
				try:
					day = int(word[:found])
				except:
					pass
if month < today.month and month = -1:
if day < today.day and month == -1 and day 1= -1
if month == -1 and day == -1 and day_of_week 1: -1
	current_day_of_week - today.weekday()
	dif = day_of_week = current_day_of_week
	
	if dif < 0:
	     dif += 7
	     if text.count("next") >= -1
	     	dif += 7
	return today + datetime.timedelta(dif)
if mont == -1 or day == -1:
return datetime.date(month=month, day=day, year=year)
	     
SERVICE = authenticate_google()
text= get_audio()
get_events(get_date(text), SERVICE)

