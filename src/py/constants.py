# Game building info
PLAYER_NAMES: tuple = ('Larry', 'Tamia', 'Ricardo')
NUM_OF_PLAYERS: int = len(PLAYER_NAMES) + 1
CARDS_IN_HAND: int = 7

# Card building Info
CARD_SUITS: tuple = ('♠', '♡', '♣️', '⟡')
CARD_FACES: tuple = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# ASCII Art
CARD_ART_BACK_FULL: list[str] = [
	'┌─────────┐', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'│░░░░░░░░░│', 
	'└─────────┘'
]
CARD_ART_BACK_HALF: list[str] = [
	'────┐',
	'░░░░│',
	'░░░░│',
	'░░░░│',
	'░░░░│',
	'░░░░│',
	'░░░░│',
	'░░░░│',
	'────┘'
]
CARD_ART_FACE: list[str] = [
	'┌─────────┐', 
	'│ ##      │', 
	'│         │', 
	'│         │', 
	'│    #    │', 
	'│         │', 
	'│         │', 
	'│      ## │', 
	'└─────────┘'
]

GO_FISH_TITLE: list[str] = [
	
	'       .                                          ',
	'      ":"                   ┌──────────┐          ',
	'    ___:____     |"\/"|     │ GO FISH! │          ',
	'  ,\'        `.    \\  /      └──────────┘        ',
	'  |  O        \\___/  |                           ',
	'~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~ ',
	'                                                  '
]
