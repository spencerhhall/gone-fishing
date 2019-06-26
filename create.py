# Creates a new trip and writes its contents into a new txt file, which is stored
# inside the 'trips' directory.

import trip

def create_trip():
	print("\n")
	newTrip = trip.Trip.from_input()
	print("\n")

	f = open("trips/" + newTrip.name + ".txt", "a")

	f.write(newTrip.name + "\n")
	f.write(newTrip.desc + "\n")

	for attendee in newTrip.attendees:
		f.write(attendee + "\n")

	f.write(newTrip.dateRange[0].strftime('%m/%d/%Y') + " - " + newTrip.dateRange[1].strftime('%m/%d/%Y') + "\n")
	
	f.write("\nEvents:")
	for event in newTrip.events:
		f.write("\n" + event.location)
	f.close()