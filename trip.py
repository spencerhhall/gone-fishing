# Contains code for Trip object

import datetime, event

class Trip:
    def __init__(self, name, desc, attendees, dateRange, events):
        self.name = name
        self.desc = desc
        self.attendees = attendees
        self.dateRange = dateRange
        self.events = events

    def add_attendees():
        attendees = []
        while True:
            attendees.append(input("Attendee name: "))
            if input("Continue: ") == "yes":
                continue
            else:
                break
        return attendees

    def add_date_range():
        dateRange = []
        dateRange.append(datetime.datetime.now())
        dateRange.append(datetime.datetime.now())
        return dateRange

    def add_events():
        events = []
        while True:
            events.append(event.Event.from_input())
            if input("Continue: ") == "yes":
                continue
            else:
                break
        return events

    @classmethod
    def from_input(cls):
        return cls(
            input("Trip name: "),
            input("Trip description: "),
            cls.add_attendees(),
            cls.add_date_range(),
            cls.add_events()
        )

    def print_self(self):
        print("TRIP PROPERTIES")
        print(self.name)
        print(self.desc)
        print(self.attendees)
        print(self.dateRange)
        print(self.events)