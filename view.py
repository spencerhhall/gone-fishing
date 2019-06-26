# Displays all Trips to user

from os import listdir
from os.path import isfile, join
onlyFiles = [f for f in listdir("trips/") if isfile(join("trips/", f))]

def view_trips():
	if len(onlyFiles) == 0:
		print("Sorry, there are no logged trips.")
	else:
		for trips in onlyFiles:
			print(trips)