import os

def delete_trip():
	if os.path.exists("demofile.txt"):
	  os.remove("demofile.txt")
	else:
	  print("The file does not exist")