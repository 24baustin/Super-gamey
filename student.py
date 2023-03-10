def intro_message():
	print("You have awaken in a strange land. Everything is made out of vegetables. \nThe walls, the ceiling, and even the people. You must find the portal that takes you back to your reality.\nGood Luck!")
	print("\nUse N, S, E, and W to move North, South, East, and West.")
	print("\nYou can also punch and grab things by typing punch and grab")
	start()
def start():
	win=False
	while win != True:
		Direc=input("What do you want to do?\n")
		if Direc == "N" or "n":
			pat()
		elif Direc == "S" or "s":
			print("testy")

def pat():
	print("You go down a dark hallway. Theere is a room to the East of you, or, the hallway continues to the north")