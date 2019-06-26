# Creates new Trip and Event(s) and adds them to folder

import trip

def create_trip():
	newTrip = trip.Trip.from_input()

	f = open("trips/" + newTrip.name + ".txt", "a")

	f.write(newTrip.name + "\n")
	f.write(newTrip.desc + "\n")
	for attendee in newTrip.attendees:
		f.write(attendee + "\n")
	f.write(newTrip.dateRange[0].strftime('%m/%d/%Y') + " - " + newTrip.dateRange[1].strftime('%m/%d/%Y') + "\n")
	f.write("\n" + "Events:")
	for event in newTrip.events:
		f.write(event.location + "\n")
	f.close()