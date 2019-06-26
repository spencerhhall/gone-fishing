# Contains code for Event object

import datetime

speciesCount = { # Number of trout and average size
	"rainbow trout": [0, 0],
	"brown trout": [0, 0],
	"cutthroat trout": [0, 0],
	"brook trout": [0, 0],
	"Arctic grayling": [0, 0],
	"bull trout": [0, 0]
}

class Event:
    def __init__(self, location, date, fish, notes):
        self.location = location
        self.date = date
        self.fish = fish
        self.notes = notes

    def add_date():
        dateRange = datetime.datetime.now()
        return dateRange

    def add_fish():
    	for species in speciesCount:
    		speciesCount[species][0] = int(input("How many " + species + " did you catch? "))
    		if(speciesCount[species][0]) != 0:
    			speciesCount[species][1] = int(input("What was the average size? "))
    	return speciesCount

    @classmethod
    def from_input(cls):
        return cls(
            input("\nNEW EVENT\nLocation: "),
            cls.add_date(),
            cls.add_fish(),
            input("Event notes: "),
        )

    def print_self(self):
        print("EVENT PROPERTIES")
        print(self.location)
        print(self.date)
        print(self.fish)
        print(self.notes)