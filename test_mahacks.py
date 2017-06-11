from bs4 import BeautifulSoup
import scraper
import event_manager

event = scraper.get_events()
 
html = open('mahacks_schedule.txt', 'r').read()
soup = BeautifulSoup(html, 'html.parser')
 
schedule_html = soup.find_all('tr')
schedule = []
reference = ['Time', 'Name']
 
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