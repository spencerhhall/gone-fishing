# Creates a new trip and writes its contents into a new txt file, which is stored
# inside the 'trips' directory.
# ! If there is an error when writing to the file, it should be deleted !
import trip

def create_trip():
    print()
    newTrip = trip.Trip.from_input()
    print()

    f = open("trips/" + newTrip.name + ".txt", "a")

    f.write(newTrip.name + "\n")
    f.write(newTrip.desc + "\n")

    for attendee in newTrip.attendees:
        f.write(attendee + ", ")

    f.write("\n"+ newTrip.dateRange[0].strftime('%m/%d/%Y') + " - " + newTrip.dateRange[1].strftime('%m/%d/%Y') + "\n")
    
    f.write("\nEvents:")
    for event in newTrip.events:
        f.write("\n" + event.location)
        f.write("\n" + event.date.strftime('%m/%d/%Y') + "\n")
        for fishRecord in event.fish:
        	if event.fish[fishRecord][0] != 0:
        		f.write(str("Caught " + event.fish[fishRecord][0]) + " " + fishRecord + " at " + str(event.fish[fishRecord][1]) + " inches on average")
        f.write("\n" + event.notes)

    f.close()