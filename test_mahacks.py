from bs4 import BeautifulSoup
import scraper
import event_manager
 
html = open('mahacks_schedule.html', 'r').read()
reference = ['Time', 'Name']
events = scraper.get_events(html, reference, row_tag='tr', col_tag='th')
event_manager.add_events(events)


# for event in schedule_html:
# 	events = {}
# 	element = event.find_all('th')
# 	# print(element)
# 	for i in range(0,2):
# 		if i == 0:
# 			events['Time'] = element[0].get_text()
# 			events['Name'] = element[1].get_text()
# 	schedule.append(events)
# print(schedule)