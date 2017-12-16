import firebase

class GameStateDatabase:
	url = 'termonopoly'
		
	def getPlayer():
		return firebase.get(GameStateDatabase.url + '/player')
	
	def incrementPlayer():
		currentPlayer = firebase.get(GameStateDatabase.url + '/player')
		currentPlayer += 1
		return firebase.put(GameStateDatabase.url + '/player', currentPlayer)
		
		

#https://github.com/shariq/firebase-python/blob/master/firebase.py
#firebase-python does not support listener/subscriber callbacks, look at above link and swap for firebase-python