# Google Calendar Automator
Named "Best Beginner Hack" at [MAHacks 2017](https://www.hackerearth.com/sprints/mahacks-spring-2017/).

Scrapes events from an HTML schedule and uploads them to Google Calendar automatically. 

# Table of Contents
1. [Introduction](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#introduction)
  a. [Problem](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#problem)
  b. [Solution](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#solution)
  c. [Installation and Usage](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#installation)
2. [How It Works](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#how-it-works)
 a. [Demo: Soccer Schedule](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#demo-soccer-schedule)
 b. [The Parts](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#the-parts)
3. [Current Issues/Limitations](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#current-issues-limitations)

# Introduction
## Problem
A lot of people like to show their schedules on their websites, but they don't have any way of reminding their users about the events. For people like me that manage all their events in Google Calendar, we have to type **every single event** in manually.

## Solution
Google Calendar Automator parses through the HTML on the site itself to find the names, dates, and other relevant information, and feeds it into the Google Calendar API for easy event creation.

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
## Demo: Soccer Schedule

## The Parts
### Schedule Scraper (scraper.py)

### Event Manager (event_manager.py)


## Current Issues/Limitations
* Date strings must be edited manually depending on the website.
  * Dates are formatted differently from website to website, so it's difficult to tell the computer which part is the day, which part is the hour, etc. I looked into dateutil, however, it isn't compatible with Python 2.7.9.
* The scraper only scrapes the part of the page with the schedule. It can't find the schedule itself.
  * For demo purposes, we only focused on scraping the portion of the HTML with the actual schedule. To use the scraper, one would have to copy and paste the schedule's HTML and place it in a text file.
* No user interface.
