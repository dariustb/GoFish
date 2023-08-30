'''test_card.py - unit tests for card.py'''

# pylint: disable=E0401, W0621

import pytest
from src.py.card import Card

@pytest.fixture
def card_number():
    '''Simple card - number face value'''
    return Card('♣️','4')

@pytest.fixture
def card_letter():
    '''Simple card - letter face value'''
    return Card('♠','J')

@pytest.fixture
def card_ten():
    '''Edge case card - face value 10'''
    return Card('♡','10')

def test_card_number_class(card_number):
    '''test attr in card_number'''
    assert card_number.d_suit  == '♣️'
    assert card_number.d_face  == '4'
    assert card_number.d_space == ' '

def test_card_letter_class(card_letter):
    '''test attr in card_letter'''
    assert card_letter.d_suit  == '♠'
    assert card_letter.d_face  == 'J'
    assert card_letter.d_space == ' '

def test_card_ten_class(card_ten):
    assert card_ten.d_suit  == '♡'
    assert card_ten.d_face  == '10'
    assert card_ten.d_space == ''

def test_suit(card_number, card_letter, card_ten):
    '''test suit method'''
    assert card_number.suit() == '♣️'
    assert card_letter.suit() == '♠'
    assert card_ten.suit()    == '♡'

def test_face(card_number, card_letter, card_ten):
    '''test face method'''
    assert card_number.face() == '4'
    assert card_letter.face() == 'J'
    assert card_ten.face()    == '10'

def test_space(card_number, card_letter, card_ten):
    '''test space method'''
    assert card_number.space() == ' '
    assert card_letter.space() == ' '
    assert card_ten.space()    == ''
