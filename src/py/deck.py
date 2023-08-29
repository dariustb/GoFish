import random
from py.card import Card
from py import constants as const

class Deck:
	def __init__(self):
		self.d_cards: list[Card] = []
		self.build()
		self.shuffle()
	
	# Deck-altering Functions
	def build(self) -> None:
		'''Builds cards in order and populates deck'''
		for suit in const.CARD_SUITS:
			for face in const.CARD_FACES:
				self.d_cards.append(Card(suit, face))

	def shuffle(self) -> None:
		'''Shuffles cards in deck with random module'''
		random.shuffle(self.d_cards)

	def deal_card(self) -> Card:
		'''Pops card from deck and returns that card'''
		return self.d_cards.pop()

	def is_empty(self) -> bool:
		'''Returns true if deck has no cards'''
		return self.d_cards == []
