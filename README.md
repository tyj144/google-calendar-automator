# Google Calendar Automator

## About
Scrapes events from a website's schedule and uploads them to Google Calendar automatically. Named "Best Beginner Hack" at [MAHacks 2017](https://www.hackerearth.com/sprints/mahacks-spring-2017/).

## Problem
A lot of people like to show their schedules on their websites, but they don't have any way of reminding their users about the events. For people like me that manage all their events in Google Calendar, we have to type **every single event** in manually.

## Solution
Google Calendar Automator parses through the HTML on the site itself to find the names, dates, and other relevant information, and feeds it into the Google Calendar API for easy event creation.

## Usage
Requires Python 2 and an authorized Google Calendar API: https://developers.google.com/google-apps/calendar/quickstart/python
```
python2.7 test_soccer.py
```
## How It Works
### Schedule Scraper (scraper.py)

### Event Manager (event_manager.py)

### Example


## Current Issues/Limitations
* Date strings must be edited manually depending on the website.
  * Dates are formatted differently from website to website, so it's difficult to tell the computer which part is the day, which part is the hour, etc. I looked into dateutil, however, it isn't compatible with Python 2.7.9.
* The scraper only scrapes the part of the page with the schedule. It can't find the schedule itself.
  * For demo purposes, we only focused on scraping the portion of the HTML with the actual schedule. To use the scraper, one would have to copy and paste the schedule's HTML and place it in a text file.
* No user interface.