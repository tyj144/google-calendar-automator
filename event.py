class Event:
	def __init__(self, attributes_array):
		self.date = attributes_array[0]
		self.time = attributes_array[1]
		
		self.opponent = attributes_array[3]
		self.location = attributes_array[4]
		self.notes = attributes_array[5]

	def __str__(self):
		return (self.date + " " + self.time + " " + self.opponent + " " + self.location)

	def get_dict(self):
		return {
      'summary': self.opponent,
      'location': self.location,
      'description': 'Game ' + self.location,
      'start': {
        'dateTime': '2017-05-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2017-05-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
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