# This file will contain the core code for running the program and main loop

import view, create, delete

print("Gone Fishing")

while True:
	decision = input("\nWould you like to \"view\", \"create\", \"delete\", or \"quit\"? ").lower()

	if decision == "view":
		view.view_trips()
	elif decision == "create":
		create.create_trip()
	elif decision == "delete":
		delete.delete_trip()
	else:
		break