from __future__ import print_function
import datetime, sys
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import traceback

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main(today = False):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    calendar_entries = []
    try:
            
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        if today:
            print ("Getting todays events")
        else:
            print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return "No upcoming events found."
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date')).encode('utf-8')
            # print (str(start).split('T')[0],datetime.datetime.now().strftime("%Y-%m-%d"))
            if today:
                if str(start).split('T')[0] == str(datetime.datetime.now().strftime("%Y-%m-%d")):
                    event_at = ':'.join(str(start).split('T')[1].split(":")[:2])
                    calendar_entries.append(str(event['summary']).replace(":"," ")+" at "+str(event_at))
            else:
                print(str(start).replace('T',' ').split(":00+")[0], "-->",event['summary'])
                calendar_entries.append(str(str(start).replace('T',' ').split(":00+")[0]+ "-->"+event['summary']))
        return 'I found total '+str(len(calendar_entries)) +' meetings today. '+ '. and '.join(calendar_entries)
    except Exception as e:
        # import sys,os
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print(exc_type, fname, exc_tb.tb_lineno)
        return traceback.format_exc()
        # return str(e)



