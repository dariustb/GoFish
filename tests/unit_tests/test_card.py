'''test_card.py - unit tests for card.py'''

# pylint: disable=E0401, W0621

import pytest
from src.py.card import Card

TEST_SUITS: tuple = ('♠', '♡', '♣️', '⟡')
TEST_FACES: tuple = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

@pytest.fixture
def card_class():
    '''Card class fixture'''
    return Card(
        suit='♡',
        face='10'
    )

def test_card_class(card_class):
    '''test attr in Card class'''
    test_space = '' if card_class.d_face == '10' else ' '
    
    assert card_class.d_suit in TEST_SUITS
    assert card_class.d_face in TEST_FACES
    assert card_class.d_space == test_space

def test_suit(card_class):
    '''test suit method'''
    assert card_class.suit() == '♡'

def test_face(card_class):
    '''test face method'''
    assert card_class.face() == '10'

def test_space(card_class):
    '''test space method'''
    assert card_class.space() == ''
