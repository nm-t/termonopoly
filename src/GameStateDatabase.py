from firebase import firebase

class GameStateDatabase:
	firebase = null
	
	def __init__(self):
		firebase = firebase.FirebaseApplication('https://termonopoly.firebaseio.com/', authentication=None)
		
	def getPlayer():
		return firebase.get('/player', None)
	
	def incrementPlayer():
		currentPlayer = firebase.get('/player', None)
		currentPlayer++
		return firebase.post('/player', currentPlayer)
		
		

#https://github.com/shariq/firebase-python/blob/master/firebase.py
#firebase-python does not support listener/subscriber callbacks, look at above link and swap for firebase-python