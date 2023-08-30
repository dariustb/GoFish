'''test_board.py - unit tests for board.py'''

# pylint: disable=E0401, W0621

from src.py import board
from src.py.player import Player
from src.py.card import Card

def test_get_player_name(monkeypatch):
    '''test get_player_name with mock inputs'''
    # Given
    inputs = iter(['Bryan', 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # When
    name = board.get_player_name()

    # Then
    assert name == 'Bryan'

def test_pick_player(monkeypatch):
    '''test pick_player() with mock input'''
    # Given
    players = [Player('Hanna'), Player('Richard', bot=False), Player('Kate', bot=False)]
    monkeypatch.setattr('builtins.input', lambda _: 'Hanna')

    # When
    human_picked_player = board.pick_player(players[2], players)
    bot_picked_player   = board.pick_player(players[0], players)

    # Then
    assert human_picked_player.name() == 'Hanna'
    assert human_picked_player.bot()
    assert bot_picked_player.name() in ['Richard', 'Kate']
    assert not bot_picked_player.bot()

def test_pick_card_with_bot():
    '''test pick_card with bot arg'''
    # Given
    bot = Player('TEST BOT', True)
    bot.d_hand = [ Card('♠','A'), Card('♠','A'), Card('♠','A') ]

    # When
    picked_card = board.pick_card(bot)

    # Then
    assert picked_card.face()  == 'A'
    assert picked_card.suit()  == '♠'
    assert picked_card.space() == ' '

def test_pick_card_with_human(monkeypatch):
    '''test pick_card with human player & mock inputs'''
    # Given
    human = Player('TEST HUMAN', False)
    human.d_hand = [ Card('♡','Q'), Card('♡','K'), Card('♡','A') ]
    monkeypatch.setattr('builtins.input', lambda _: 'Q') # Mock user input

    # When
    picked_card = board.pick_card(human)

    # Then
    assert picked_card.face()  == 'Q'
    assert picked_card.suit()  == '♡'
    assert picked_card.space() == ' '
