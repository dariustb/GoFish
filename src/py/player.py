'''player.py - player related class'''

# pylint: disable=R1710

from py.card import Card
from py.deck import Deck
from py import constants as const

class Player:
    '''Player hand related attr/functions'''
    def __init__(self, name='Player', bot=True):
        self.d_name: str = name
        self.d_bot: bool = bot
        self.d_hand: list[Card] = []

    # Getter Functions
    def name(self) -> str:
        '''Getter for name'''
        return self.d_name

    def bot(self) -> bool:
        '''Getter for bot'''
        return self.d_bot

    def hand(self) -> list:
        '''Getter for hand'''
        return self.d_hand

    # Hand-altering Functions
    def take_card(self, card:Card) -> None:
        '''Takes card given'''
        self.d_hand.append(card)

    def draw_card(self, deck:Deck) -> None:
        '''Takes card and adds to hand'''
        self.take_card(deck.deal_card())

    def give_card(self, face:str) -> Card:
        '''Takes card with face from player hand and returns card'''
        for index, card in enumerate(self.d_hand):
            if face.upper() == card.face():
                return self.d_hand.pop(index)

    def give_player_card(self, other, card:Card) -> None:
        '''Removes card from self's hand and appends to other's hand''' 
        temp_card = self.give_card(card.face())
        other.take_card(temp_card)

    def toss_card_pair(self, face:str=None) -> bool:
        '''Removes matching-faced cards from hand'''
        card_pair = []

        if face is None:
            face = self.find_card_pair()
        if face is None:
            return False

        for card_idx, card in enumerate(self.d_hand):
            if face.upper() == card.face():
                card_pair.append(card_idx)
                if len(card_pair) == 2:
                    break
        self.d_hand.pop(card_pair.pop())
        self.d_hand.pop(card_pair.pop())

        return True

    def toss_all_card_pairs(self) -> None:
        '''Searches for all pairs in hand and tosses them'''
        is_pair_found = self.toss_card_pair()
        while is_pair_found:
            is_pair_found = self.toss_card_pair()

    # Search Functions
    def find_card_pair(self) -> str:
        '''Returns face of card pair in hand'''
        for lower_bound in self.d_hand:
            for upper_bound in self.d_hand:
                if lower_bound.face() == upper_bound.face():
                    return lower_bound.face()
        return None

    # Status Functions
    def is_card_in_hand(self, face:str) -> bool:
        '''Returns if card with face values is in hand'''
        for card in self.d_hand:
            if card.face() == face:
                return True
        return False

    def is_hand_empty(self) -> bool:
        '''Returns true if no cards are in hand'''
        return not self.d_hand

    # Print Functions
    def print_hidden_hand(self) -> None:
        '''Prints card backs of player hand'''
        print(self.d_name+':')
        for line_idx, line in enumerate(const.CARD_ART_BACK_FULL):
            for card_idx in range(len(self.d_hand)):
                if card_idx == 0:
                    print(line, end=' ')
                else:
                    print(const.CARD_ART_BACK_HALF[line_idx], end=' ')
            print()
        print()

    def print_visible_hand(self) -> None:
        '''Prints card fronts of player hand'''
        print(self.name()+':')
        for line_idx, line in enumerate(const.CARD_ART_FACE):
            for card in self.hand():
                if   line_idx == 1:
                    print(line.replace('##', card.face()+card.space()), end=' ')
                elif line_idx == 4:
                    print(line.replace('#', card.suit()), end=' ')
                elif line_idx == 7:
                    print(line.replace('##', card.space()+card.face()), end=' ')
                else:
                    print(line, end=' ')
            print()
        print()
