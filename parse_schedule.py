from bs4 import BeautifulSoup
import re
from event import Event

def get_events():
	html = open('schedule.txt', 'r').read()
	soup = BeautifulSoup(html, 'html.parser')

	schedule = []
	schedule_html = soup.find_all(class_=re.compile('^seasonRowItem'))

	for event in schedule_html:
		attributes = []
		for element in event.find_all('p'):
			attributes.append(element.get_text().strip(' \t\n\r'))
		schedule.append(attributes)
		
	reference = ['Date', 'Time', 'Home or Away', 'Opponent', 'Location', 'Notes', '']

	events = []

	for event in schedule:
		events.append(Event(event))

	return events[0].get_dict()
	# for event in events:
	# 	print(event.getDict())