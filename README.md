# Google Calendar Automator
Named "Best Beginner Hack" at [MAHacks 2017](https://www.hackerearth.com/sprints/mahacks-spring-2017/).

Scrapes events from an HTML schedule and uploads them to Google Calendar automatically. 

# Table of Contents
* [Introduction](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#introduction)
* [Installation and Usage](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#installation-and-usage)
* [How It Works](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#how-it-works)
  * [Executing the Plan](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#executing-the-plan-testsoccerpy)
  * [The Parts](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#the-parts)
* [Current Issues/Limitations](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#current-issueslimitations)

# Introduction
**Problem**: A lot of people like to show their schedules on their websites, but they don't have any way of reminding their users about the events. For people like me that manage all their events in Google Calendar, we have to type **every single event** in manually.

**Solution**: Google Calendar Automator parses through the HTML on the site itself to find the names, dates, and other relevant information, and feeds it into the Google Calendar API for easy event creation.

# Installation and Usage
## Installation
Requires Python 2.
1. Clone the repository.
```
git clone https://github.com/tyj144/google_calendar_automator.git
```
2. Authorize the Google Calendar API: https://developers.google.com/google-apps/calendar/quickstart/python

## Usage
```
python2.7 test_soccer.py
```
# How It Works
Google Calendar Automator provides a generalized solution to stripping a website's HTML schedule and adding the contents to Google Calendar.

This general solution is based on the fact that all HTML schedules are organized in a tables, with rows and columns. Every row signifies an event, and every column signifies an attribute (e.g. date, time, location, etc.)

Say for example, you see a [schedule](http://nashuanorthathletics.com/main/teamschedule/id/3695990/seasonid/4115615) online for your high school's soccer games. 

![Nashua North's soccer schedule](https://github.com/tyj144/google_calendar_automator/blob/master/demo/schedule.png)
However, they didn't give you an easy way to add them to your calendar, and adding every single one by hand is a slow, tedious process, especially if you have 16 games in a season.

However, the creators must have organized the events themselves while writing the HTML for the schedule, otherwise the schedule itself would not be organized.

**vs. Merrimack**
```html
...
<div class="seasonRowItem_7_1_1_7 arrowAfter" ssfilter="1" style="display:block;overflow-x:auto;">
   ...
       <p class="seasonDefaultText seasonTextAway ">
        Fri 08/26
       </p>
      ...
       <p class="seasonDefaultText seasonTextAway ">
        4:00 pm
       </p>
      ...
       <p class="seasonDefaultText seasonTextAway ">
        Away
       </p>
      ...
       <p class="seasonDefaultText seasonTextAway ">
        @ Merrimack High School
       </p>
      ...
       <p class="seasonDefaultText seasonTextAway ">
        GPS Turf Fields
       </p>
      ...
  </div>
...
```
As you can see, each game is marked with a ```<div class="seasonRowItem..."> tag```, which tells the website to make a new **row** in the table for the game.

Each **column** has some text that we would like to use, which is kept in the ```<p>``` tag.

If we filter the table's HTML so that we only get the sections with ```<div class="seasonRowItem..."> tag```, then we'll have all the **rows** of the table, which are all 16 games. 

Within each row, we can pull out the event information by filtering by the ```<p>``` tag and putting each string in a list. The first ```<p>``` gives us the date, the second the time, the third whether it's home or away, etc.

Since all events in the table are organized in the same way, we always know that the date is first, the time is second, etc. That means when Google Calendar asks for an event's date, we can pull it out of the first column. When Google Calendar asks for the event's location, we can pull it out of the fifth column.

We can then put all this information into JSON format and upload the event through the Google Calendar API. Rinse and repeat for each event. 

## Executing the Plan (test_soccer.py)
Let's actually upload our soccer games. We'll do this by making a script called ```test_soccer.py```.

We need a scraper to get our events and an event manager to upload them, which we'll create later. We'll also import re to use regular expressions because we have that pesky "seasonRowItem..." with a number that keeps changing.
```python
import scraper
import event_manager
import re
```

First, we'll get all of our events by scraping them off the page. We'll do this by using our scraper's ```get_events()``` function and storing the results in a variable called events. 

```python
events = scraper.get_events(html, reference, row_class=re.compile('^seasonRowItem'), col_tag='p')
```

Then, we'll add the events to our calendar by passing the events to our event manager, which has a function `add_events()` that will upload the events for us.
```python
event_manager.add_events(events)
```

## The Parts
### Schedule Scraper (scraper.py)
All schedules online are organized in some kind of table. Any HTML table will have a tag/class that marks its rows, and another tag/class that marks its columns.

Scraper.py contains one function, ```get_events()```, which takes the following paramaters:
```python
def get_events(html, reference, row_tag=None, row_class=None, col_tag=None, col_class=None):
```
**Returns** a list of events, each one in JSON format (the format used by the Google Calendar API).
* ```html```: the HTML file with the schedule table
* ```reference```: the top row of the table, which tells us what each column stands for
  * This is necessary because most sites don't mark what each column is within the tag, but they still keep them in a specific order. For example, the computer doesn't know which ```<p>``` tag is the date. However, the top row of the table tells us that the date is the 1st column, and thus always the first ```<p>``` tag.
* ```row_tag/row_class```: specifies which tag is the row
* ```col_tag/col_class```: specifies which tag is the column

The scraper will find the events by first splitting the HTML table into rows. It does this by using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), a Python library for parsing HTML, to filter the HTML into a list of tags, each one of which contains everything within the starting and closing tags of each row. 

Then, it splits the events by column and uses the reference to mark what each column stands for in a dictionary:
```python
{'Name': u'@ Merrimack High School', 'Home or Away': u'Away', 'Notes': u'', 'Location': u'GPS Turf Fields', 'Time': u'4:00 pm', 'Date': u'Fri 08/26'}
```

#### The Event Object (event.py)
```python
def __init__(self, attributes):
```
Contains an event object, which takes the dictionary from before and converts it to a JSON format that the Google Calendar API can use.

The scraper returns a list of JSON dictionaries, each dictionary containing information about each event (in this case, each game).

---

### Event Manager (event_manager.py)
Takes the list of events in JSON format from the scraper and uploads each one to Google Calendar.

The main function in the event manager is `add_events()`, which accepts the list of JSON events.
```python
def add_events(events_to_add):
```

The heart of the event_manager lies in the following lines:
```python
for event in events_to_add:
    service.events().insert(calendarId='primary', body=event).execute()
```
   
## Current Issues/Limitations
* Date strings must be edited manually depending on the website.
  * Dates are formatted differently from website to website, so it's difficult to tell the computer which part is the day, which part is the hour, etc. I looked into dateutil, however, it isn't compatible with Python 2.7.9.
* The scraper only scrapes the part of the page with the schedule. It can't find the schedule itself.
  * For demo purposes, we only focused on scraping the portion of the HTML with the actual schedule. To use the scraper, one would have to copy and paste the schedule's HTML and place it in a text file.
* No user interface.
