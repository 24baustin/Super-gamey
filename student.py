from numpy import array
import pickle
from Rooms import rooms, MOVEMENT

ACTIONS=("quit",
		 "save",
		 "load",
		 "get",
		 "use",
		 "move")
class Player():
	def __init__(self):
						#x, y, z
		self.position = (0, 0, 0)
		self.inventory = []
		self.name = input("What name would you like to be called?\n").title()
		print(f"{self.name} is starting a very healthy adventure")

	def move(self, move):
		self.position = tuple(array(self.position)+MOVEMENT.get(move,array([0,0,0])))
def valid_input(prompt = "What would you like to do? "):
	print("\t--COMMANDS--")
	response = None
	while response not in ACTIONS:
		print(f"Actions:\n{ACTIONS}")
		response = input(prompt).lower()
	return response

def save(player):
	with open('game.dat','wb') as f:
		pickle.dump(player,f)
		pickle.dump(rooms,f)
	print("Game saved!")
def load():
	global player
	global rooms
	try:
		with open("game.dat",'rb') as f:
			player = pickle.load(f)
			rooms = pickle.load(f)
		print("Game loaded!")
	except FileNotFoundError:
		print("Game file not found!")
player = Player()
def main(player):
	choice = None
	while choice != "quit":
		#unpack current room variables
		room = rooms.get(player.position, "Uh-oh, that was an invalid room setting!")
		print(room.description())
		choice = valid_input()
		if choice == "quit":
			print("Thanks for playing!")
		elif choice == "save":
			save(player)
		elif choice == "load":
			load()
		elif choice == "get":
			room.get_item(player)
		elif choice == "use":
			room.use_item(player)
		elif choice == "move":
			room.move(player)
if __name__ == "__main__":
	main(player)




#def start():
#	print("You have awaken in a strange land. Everything is made out of vegetables. \nThe walls, the ceiling, and even the people. You must find the portal that takes you back to your reality.\nGood Luck!")
#	print("\nUse N, S, E, and W to move North, South, East, and West.")
#	print("\nYou can also punch and get things by typing punch and get")
#	win=False
#	while win != True:
#		Direc=input("What do you want to do?\n")
#		if Direc == "N" or "n":
#			pat_peep()
#		elif Direc == "S" or "s":
#			print("south")
#		elif Direc == "E" or "e":
#			print("east")
#		elif Direc == "W" or "w":
#			print("west")
	
	
#def pat_peep():
#	print("You go down a dark hallway. Theere is a room to the East of you, or, the hallway continues to the north")