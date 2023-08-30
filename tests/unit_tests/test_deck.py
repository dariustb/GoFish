'''test_deck.py - unit tests for deck.py'''

# pylint: disable=E0401, W0621

import pytest
import copy
from src.py.deck import Deck

@pytest.fixture
def deck_class():
    '''Deck class fixture'''
    return Deck()

def test_deck_class(deck_class):
    '''test attr in Deck class'''
    assert type(deck_class.d_cards) == list
    assert len(deck_class.d_cards) == 52

def test_build(deck_class):
    '''test suit method'''
    # Given
    deck_class.d_cards = []
    assert deck_class.d_cards == []

    # When
    deck_class.build()

    # Then
    assert deck_class.d_cards != []
    assert len(deck_class.d_cards) == 52


def test_shuffle(deck_class):
    '''test shuffle method'''
    # Given
    deck_class.d_cards = []

    # When
    deck_class.build()
    build_cards = copy.copy(deck_class.d_cards)
    deck_class.shuffle()

    # Then
    assert (deck_class.d_cards is not build_cards)
