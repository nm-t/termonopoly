import firebase
#todo add instantiation so that state can be tracked and monitorPlayers can be turned off
class GameStateDatabase:
	url = 'termonopoly'
	
	def __init__(self):
		self.playerSubscription = null
	
	def getPlayer():
		return firebase.get(GameStateDatabase.url + '/player')
	
	def incrementPlayer():
		currentPlayer = firebase.get(GameStateDatabase.url + '/player')
		currentPlayer += 1
		return firebase.put(GameStateDatabase.url + '/player', currentPlayer)
		
	def monitorPlayers(callbackMethod):
		playerSubscription = firebase.subscriber(GameStateDatabase.url + '/player', callbackMethod)
		playerSubscription.start()
		print("subscription started");
		firebase.put(GameStateDatabase.url + '/player', 1)
		print("player set to 1")
		firebase.put(GameStateDatabase.url + '/player', 3)
		print("player set to 3")
		firebase.put(GameStateDatabase.url + '/player', 2)
		print("player set to 2")
		#playerSubscription.stop()		
		#print("subscription stopped")