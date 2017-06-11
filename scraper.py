from bs4 import BeautifulSoup
import re
from event import Event

'''
	Takes an html file, the row tag for the html, and a way to identify the column
'''
def get_events(html, reference, row_tag=None, row_class=None, col_tag=None, col_class=None):
	soup = BeautifulSoup(html, 'html.parser')

	events = []

	# take in either a column tag or a class selector
	if row_tag:
		schedule_html = soup.find_all(row_tag)
	else:
		schedule_html = soup.find_all(class_=row_class)

	for event in schedule_html:
		attributes = []

		# choose between column tags and class selectors
		if col_tag:
			columns = event.find_all(col_tag)
		else:
			columns = event.find_all(class_=col_class)

		for element in columns:
			attributes.append(element.get_text().strip(' \t\n\r'))
		events.append(attributes)

	# turn attributes into dictionaries
	schedule = []
	for event in events:
		event_dict = {}
		for i in range(0, len(reference)):
			event_dict[reference[i]] = event[i]
		schedule.append(event_dict)

	print(schedule)

	events_to_add = []
	# create event objects from dictionaries
	for event in schedule:
		events_to_add.append(Event(event))

	print(events_to_add[0].datetime)

	return [events_to_add[0].get_dict()]
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