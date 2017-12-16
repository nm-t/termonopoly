import firebase
#todo add instantiation so that state can be tracked and monitorPlayers can be turned off
class GameStateDatabase:
	url = 'termonopoly'
	
	def __init__(self):
		self.playerSubscription = 
	
	def getPlayer():
		return firebase.get(GameStateDatabase.url + '/player')
	
	def incrementPlayer():
		currentPlayer = firebase.get(GameStateDatabase.url + '/player')
		currentPlayer += 1
		return firebase.put(GameStateDatabase.url + '/player', currentPlayer)
		
	def monitorPlayers(callbackMethod):
		playerSubscription = firebase.subscriber(GameStateDatabase.url + '/player', callbackMethod)
		playerSubscription.start()