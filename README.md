# Google Calendar Automator
[MAHacks 2017](https://www.hackerearth.com/sprints/mahacks-spring-2017/) prize winner.

Finds calendar events within HTML and uploads them to Google Calendar.

* **Note**: I built a generalized solution to finding and scraping HTML tables, which can be found here: https://github.com/tyj144/table-scraper

# Table of Contents
* [Introduction](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#introduction)
* [Installation](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#installation-and-usage)
* [Demo](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#demo)
* [How It Works](https://github.com/tyj144/google_calendar_automator/blob/master/README.md#how-it-works)
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
2. Install the requirements and authorize the Google Calendar API: https://developers.google.com/google-apps/calendar/quickstart/python
```
pip install -r requirements.txt
```

# Demo
```
python2.7 test_soccer.py
```

Calling `python2.7 test_soccer.py` within the directory will run the script, which looks something like this:
![Running test_soccer.py](https://github.com/tyj144/google-calendar-automator/blob/master/demo/terminal.png)

If running the script for the first time, you may need to log in to authorize Google Calendar Automator.

Once the script has completed, the calendar will look something like this:
![Completed event creation](https://github.com/tyj144/google-calendar-automator/blob/master/demo/results.png)

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
As you can see, each game is marked with a ```<div class="seasonRowItem...">``` tag, which tells the website to make a new **row** in the table for the game.

Each **column** has some text that we would like to use, which is kept in the ```<p>``` tag.

If we filter the table's HTML so that we only get the sections with ```<div class="seasonRowItem...">``` tag, then we'll have all the **rows** of the table, which are all 16 games. 

Within each row, we can pull out the event information by filtering by the ```<p>``` tag and putting each string in a list. The first ```<p>``` gives us the date, the second the time, the third whether it's home or away, etc.

Since all events in the table are organized in the same way, we always know that the date is first, the time is second, etc. That means when Google Calendar asks for an event's date, we can pull it out of the first column. When Google Calendar asks for the event's location, we can pull it out of the fifth column.

We can then put all this information into JSON format and upload the event through the Google Calendar API. Rinse and repeat for each event. 

# Current Issues/Limitations
* <s>Date strings must be edited manually depending on the website.
  * Dates are formatted differently from website to website, so it's difficult to tell the computer which part is the day, which part is the hour, etc. I looked into dateutil, however, it isn't compatible with Python 2.7.9.</s>
  * Date string parsing is implemented in [table-scraper](https://github.com/tyj144/table-scraper).
* <s>The scraper only scrapes the part of the page with the schedule. It can't find the schedule itself.
  * For demo purposes, we only focused on scraping the portion of the HTML with the actual schedule. To use the scraper, one would have to copy and paste the schedule's HTML and place it in a text file.</s>
  * Table detection within HTML is implemented in [table-scraper](https://github.com/tyj144/table-scraper).
