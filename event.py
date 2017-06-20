from datetime import datetime, timedelta

class Event:
  def __init__(self, attributes):
    print(attributes)
    if 'Date' in attributes:
      self.date = attributes['Date']
    else:
      self.date = datetime.today().date().strftime('%a %m/%d')
    self.time = attributes['Time']
    self.datetime = self.datetime = datetime.strptime(self.date + "/2016 " + self.time, 
      "%a %m/%d/%Y %I:%M %p")
      # "%a %m/%d/%Y %I%p")

    if 'Name' in attributes:
      self.name = attributes['Name']
    else:
      self.name = 'Event'
    
    if 'Location' in attributes:
      self.location = attributes['Location']
    else:
      self.location = ''
    
    if 'Notes' in attributes:
      self.notes = attributes['Notes']
    else:
      self.notes = ''

  def __str__(self):
		return (self.date + " " + self.time + " " + self.name + " " + self.location)

  def get_dict(self):
		return {
      'summary': self.name,
      'location': self.location,
      'description': '',
      'start': {
        'dateTime': self.datetime.isoformat(),
        'timeZone': 'America/New_York',
      },
      'end': {
        'dateTime': (self.datetime + timedelta(hours=2)).isoformat(),
        # 'dateTime': '2017-05-28T17:00:00-07:00',
        'timeZone': 'America/New_York',
      },
      # 'recurrence': [
      #   'RRULE:FREQ=DAILY;COUNT=2'
      # ],
      # 'attendees': [
      #   {'email': 'lpage@example.com'},
      #   {'email': 'sbrin@example.com'},
      # ],
      'reminders': {
        'useDefault': True,
        # 'overrides': [
        #   {'method': 'email', 'minutes': 24 * 60},
        #   {'method': 'popup', 'minutes': 10},
        # ],
      },
    }