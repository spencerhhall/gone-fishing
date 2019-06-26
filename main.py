# Contains the loop for the program.

import view-delete, create

print("Gone Fishing\n")

while True:
    choice = input("Would you like to \'view\' logged trips, \'create\' a new trip," +
    " \'delete\' a trip, or \'quit\'? ").lower()

    if choice == "view":
        view.v_d_trips(True)
    elif choice == "create":
        create.create_trip()
    elif choice == "delete":
        view.v_d_trips(False)
    elif choice == "quit":
        break