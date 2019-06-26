# Displays all files in the 'trips' directory (if they exist) and allows the user
# to read or delete a chosen file.
import os
from os import listdir
from os.path import isfile, join

def v_d_trips(view):
    tripFiles = [f for f in listdir("trips/") if isfile(join("trips/", f))]
    
    if len(tripFiles) == 0:
        print("\nSorry, there are no logged trips.")
    else:
        n = 0
        print("\nLogged Trips:")
        for trips in tripFiles:
            n += 1
            print("(" + str(n) + ") " + trips)

        choice = input("Would you like to choose a file? ").lower() == "yes"
        while choice:
            index = int(input("Please choose a valid index: "))

            if index < 1 or index > len(tripFiles):
                print("Index is invalid.")
                continue
            else:
                if view:
                    f = open("trips/" + tripFiles[index - 1], "r")
                    print("\n" + f.read())
                    f.close()
                else:
                    os.remove("trips/" + tripFiles[index - 1])
                break

        print()