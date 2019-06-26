# Contains the loop for the program.

import view, create, delete

print("Gone Fishing\n")

while True:
	choice = input("Would you like to \'view\' logged trips, \'create\' a new trip," +
		" \'delete\' a trip, or \'quit\'? ").lower()

	if choice == "view":
		view.view_trips()
	elif choice == "create":
		create.create_trip()
	elif choice == "delete":
		delete.delete_trip()
	elif choice == "quit":
		break