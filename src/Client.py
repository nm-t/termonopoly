from database import GameStateDatabase
playerNum = GameStateDatabase.getPlayer()
print("Player number is " + str(playerNum))
GameStateDatabase.incrementPlayer()
playerNum = GameStateDatabase.getPlayer()
print("Player number is now " + str(playerNum))
