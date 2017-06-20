from bs4 import BeautifulSoup
import re
from event import Event

'''
	Takes an html table, a way to identify the table's row, and a way to identify the column
'''
def get_events(html, reference, row_tag=None, row_class=None, col_tag=None, col_class=None):
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

	# turn attributes into dictionaries
	schedule = []
	for event in events:
		event_dict = {}
		for i in range(0, len(reference)):
			event_dict[reference[i]] = event[i]
		schedule.append(event_dict)

	events_to_add = []
	# create event objects from dictionaries
	for event in schedule:
		events_to_add.append(Event(event))

	schedule = []
	for event in events_to_add:
		schedule.append(event.get_dict())

	return schedule
	# for event in events:
	# 	print(event.getDict())

# def get_events():
# 	html = open('soccer_schedule.txt', 'r').read()
# 	soup = BeautifulSoup(html, 'html.parser')

# 	schedule = []
# 	schedule_html = soup.find_all(class_=re.compile('^seasonRowItem'))

# 	for event in schedule_html:
# 		attributes = []
# 		for element in event.find_all('p'):
# 			attributes.append(element.get_text().strip(' \t\n\r'))
# 		schedule.append(attributes)
		
# 	reference = ['Date', 'Time', 'Home or Away', 'Opponent', 'Location', 'Notes', '']

# 	events = []

# 	for event in schedule:
# 		events.append(Event(event))

# 	print(events[0].datetime)

# 	return [events[0].get_dict()]
# 	# for event in events:
# 	# 	print(event.getDict())

# print(get_events())