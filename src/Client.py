from database import GameStateDatabase

def printer():
	print("player detected")
	
	
playerNum = GameStateDatabase.getPlayer()
print("Player number is " + str(playerNum))
GameStateDatabase.incrementPlayer()
playerNum = GameStateDatabase.getPlayer()
print("Player number is now " + str(playerNum))
GameStateDatabase.monitorPlayers(printer)

