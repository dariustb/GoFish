'''test_player.py - unit tests for player.py'''

# pylint: disable=E0401, W0621

import pytest
from src.py.player import Player
from src.py.card import Card
from src.py.deck import Deck

@pytest.fixture
def player():
    '''Player fixture'''
    return Player('Bryan', bot=False)

def test_player_class(player):
    '''Test player attr'''
    assert player.d_name == 'Bryan'
    assert not player.d_bot
    assert not player.d_hand

def test_name(player):
    '''Test name method'''
    assert player.name() == 'Bryan'

def test_bot(player):
    '''Test bot method'''
    assert not player.bot()

def test_hand(player):
    '''Test hand method'''
    assert not player.hand()

def test_take_card(player):
    '''Test take_card method'''
    # Given
    player.d_hand = []
    card = Card('⟡', '5')

    # When
    player.take_card(card)
    taken_card = player.hand()[0]

    # Then
    assert len(player.hand()) == 1
    assert taken_card.face()  == '5'
    assert taken_card.suit()  == '⟡'
    assert taken_card.space() == ' '

def test_draw_card(player):
    '''Test draw_card method'''
    # Given
    deck = Deck()
    player.d_hand = []

    # When
    player.draw_card(deck)

    # Then
    assert len(player.hand()) == 1
    assert len(deck.d_cards)  == 52 - 1

def test_give_card(player):
    '''Test give_card method'''
    # Given
    player.d_hand = [Card('⟡', '5')]

    # When
    given_card = player.give_card('5')

    # Then
    assert given_card.face()  == '5'
    assert given_card.suit()  == '⟡'
    assert given_card.space() == ' '

def test_give_player_card(player):
    '''test give_player_card method'''
    # Given
    other_player = Player('OtherGuy')
    card_to_give = Card('⟡','5')
    player.d_hand = [card_to_give]

    # When
    player.give_player_card(other_player, card_to_give)

    # Then
    assert not player.d_hand
    assert len(other_player.d_hand)       == 1
    assert other_player.d_hand[0]         == card_to_give
    assert other_player.d_hand[0].face()  == '5'
    assert other_player.d_hand[0].suit()  == '⟡'
    assert other_player.d_hand[0].space() == ' '

def test_toss_card_pair_with_face(player):
    '''Test toss_card_pair method'''
    # Given
    player.d_hand = [Card('⟡','5'), Card('♣️','5')]

    # When/Then
    assert player.toss_card_pair('5')
    assert not player.hand()


def test_toss_card_pair_without_face(player):
    '''Test toss_card_pair method'''
    # Given
    player.d_hand = [Card('⟡','5'), Card('♣️','5')]

    # When/Then
    assert player.toss_card_pair()
    assert not player.hand()

def test_toss_all_card_pairs(player):
    '''Test toss_all_card_pairs method'''
    # Given
    player.d_hand = [Card('⟡','5'), Card('♣️','5'), Card('⟡','Q'), Card('♣️','Q'), Card('♠','A')]

    # When
    player.toss_all_card_pairs()

    # Then
    assert len(player.hand())       == 1
    assert player.hand()[0].face()  == 'A'
    assert player.hand()[0].suit()  == '♠'
    assert player.hand()[0].space() == ' '

def test_find_card_pair(player):
    '''Test find_card_pair method'''
    # Given
    player.d_hand = [Card('⟡','5'), Card('♣️','5'), Card('⟡','Q'), Card('♣️','Q'), Card('♠','A')]

    # When
    pair_face = player.find_card_pair()

    # Then
    assert pair_face == '5' # 5 is the first pair found and is returned

def test_is_card_in_hand(player):
    '''Test is_card_in_hand method'''
    # Given
    player.d_hand = [Card('⟡','5')]

    # When/Then
    assert player.is_card_in_hand('5')
    assert not player.is_card_in_hand('6')

def test_is_hand_empty_when_empty(player):
    '''Test is_hand_empty method'''
    # Given
    player.d_hand = []

    # When/Then
    assert player.is_hand_empty()

def test_is_hand_empty_when_not_empty(player):
    '''Test is_hand_empty method'''
    # Given
    player.d_hand = [Card('⟡','5')]

    # When/Then
    assert not player.is_hand_empty()
