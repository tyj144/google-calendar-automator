# Google Calendar Automator
Named "Best Beginner Hack" at [MAHacks 2017](https://www.hackerearth.com/sprints/mahacks-spring-2017/).

Scrapes events from an HTML schedule and uploads them to Google Calendar automatically. 

# Table of Contents
* [Introduction](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#introduction)
* [Installation and Usage](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#installation-and-usage)
* [How It Works](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#how-it-works)
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

## The Parts
### Schedule Scraper (scraper.py)
All schedules online are organized in some kind of table. Any HTML table will have a tag/class that marks its rows, and another tag/class that marks its columns.
### Event Manager (event_manager.py)

## Current Issues/Limitations
* Date strings must be edited manually depending on the website.
  * Dates are formatted differently from website to website, so it's difficult to tell the computer which part is the day, which part is the hour, etc. I looked into dateutil, however, it isn't compatible with Python 2.7.9.
* The scraper only scrapes the part of the page with the schedule. It can't find the schedule itself.
  * For demo purposes, we only focused on scraping the portion of the HTML with the actual schedule. To use the scraper, one would have to copy and paste the schedule's HTML and place it in a text file.
* No user interface.
