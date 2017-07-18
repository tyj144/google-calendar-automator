# Google's default imports
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# Project's imports
from bs4 import BeautifulSoup

import re
from datetime import datetime, timedelta

try:
    import argparse
    # flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar Automator'

def get_events(html, reference, row_tag=None, row_class=None, col_tag=None, col_class=None):
	"""Takes an html table, a way to identify the table's row, and a way to identify the column
	"""

	soup = BeautifulSoup(html, 'html.parser')

	events = []

	# Split the HTML into a list of the table's rows
	# This will split the schedule into events, which are stored in a list
	if row_tag:
		schedule_html = soup.find_all(row_tag)
	else:
		schedule_html = soup.find_all(class_=row_class)

	# Within each event, split by attribute (e.g. date, time, location, etc.)
	for event in schedule_html:
		attributes = []

		# Split by column
		if col_tag:
			columns = event.find_all(col_tag)
		else:
			columns = event.find_all(class_=col_class)

		# Stores these attributes in a list, each list is its own event
		for element in columns:
			attributes.append(element.get_text().strip(' \t\n\r'))
		# put each event into the list called events
		events.append(attributes)

	# turn attributes into dictionaries, which will be the arguments for create_json
	jsons = []
	for event in events:
		event_dict = {}
		for i in range(0, len(reference)):
			event_dict[reference[i]] = event[i]
		jsons.append(create_json(**event_dict))

	return jsons

def create_json(name='', date=datetime.today().date().strftime('%a %m/%d'),
	length_hours=2, time=datetime.today().time().strftime('%I:%M %p'),
	location='', description='', remind=True, 
	# catches all the extra arguments to avoid a TypeError (https://stackoverflow.com/a/11065434/5026239)
	**extras):
	
	"""Takes a set of arguments and creates a JSON for the Google Calendar API to use.
	"""

	dt = datetime.strptime(date + "/2016 " + time, 
      "%a %m/%d/%Y %I:%M %p")

	json = {
		'summary': name,
		'location': location,
		'description': '',
		'start': {
			'dateTime': dt.isoformat(),
			'timeZone': 'America/New_York',
		},
		'end': {
			'dateTime': (dt + timedelta(hours=length_hours)).isoformat(),
			# 'dateTime': '2017-05-28T17:00:00-07:00',
			'timeZone': 'America/New_York',
		},
		'reminders': {
		'useDefault': remind,
  		}
	}

	return json

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def add(events):
    """Adds JSON events from events_to_add onto Google Calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    for event in events:
    	name = event['summary']
        event = service.events().insert(calendarId='primary', body=event).execute()
        print("Added " + name + " at " + event.get('htmlLink'))