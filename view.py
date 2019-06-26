# Displays all files in the 'trips' directory (if they exist) and allows the user
# to read a file, which is printed to the console.

from os import listdir
from os.path import isfile, join

def view_trips():
	tripFiles = [f for f in listdir("trips/") if isfile(join("trips/", f))]
	
	if len(tripFiles) == 0:
		print("\nSorry, there are no logged trips.")
	else:
		n = 0
		print("\nLogged Trips:")
		for trips in tripFiles:
			n += 1
			print("(" + str(n) + ") " + trips)

		readOption = input("Would you like to read a file? ").lower() == "yes"
		while readOption:
			choice = int(input("Please choose a valid index: "))
			if choice < 1:
				print("Index is too low.")
				continue
			elif choice > len(tripFiles):
				print("Index is too high.")
				continue
			else:
				f = open("trips/" + tripFiles[choice - 1], "r")
				print("\n" + f.read())
				f.close()
				break
		print("\n")