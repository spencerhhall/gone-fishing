# Displays all Trips to user

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def view_trips():
	print(onlyfiles)