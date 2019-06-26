# Contains the loop for the program.
import view_delete, create

print(">¬=∫∫•_ Gone Fishing >¬=∫∫•_\n")

while True:
    choice = input("Would you like to \'view\' logged trips, \'create\' a new trip," +
    " \'delete\' a trip, or \'quit\'? ").lower()

    if choice == "view":
        view_delete.v_d_trips(True)
    elif choice == "create":
        create.create_trip()
    elif choice == "delete":
        view_delete.v_d_trips(False)
    elif choice == "quit":
        break