import scraper
import event_manager
import re

# get this later from top row
reference = ['Date', 'Time', 'Home or Away', 'Name', 'Location', 'Notes', '']
html = open('soccer_schedule.html', 'r').read()
events = scraper.get_events(html, reference, row_class=re.compile('^seasonRowItem'), col_tag='p')
event_manager.add_events(events)