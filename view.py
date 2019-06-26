# Displays all Trips to user

from os import listdir
from os.path import isfile, join

def view_trips():
	onlyFiles = [f for f in listdir("trips/") if isfile(join("trips/", f))]
	
	if len(onlyFiles) == 0:
		print("Sorry, there are no logged trips.")
	else:
		for trips in onlyFiles:
			print(trips)