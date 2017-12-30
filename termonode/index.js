var firebase = require("firebase");
var config = {
	apiKey: "AIzaSyDhQ6VdIQC3GpjRULCdbuhc5WYgtuRbw8w",
    authDomain: "termonopoly.firebaseapp.com",
    databaseURL: "https://termonopoly.firebaseio.com",
    storageBucket: "termonopoly.appspot.com",
};
var playerNumber;
firebase.initializeApp(config);
firebase.database().ref('/player').on('value', function(snapshot) {
	if (playerNumber === null) {
		playerNumber = snapshot.val();
		console.log('Player number set to ' + snapshot.val());
		firebase.database().ref('/player').set(snapshot.val() + 1);
	}
	if (snapshot.val() === 4) {
		firebase.database().ref('/player').off();
	}
});