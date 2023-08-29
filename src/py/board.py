'''board.py - UI and game mechanics-based library'''

import random
from py.player import Player
from py.card   import Card
from py import constants as const

def print_title() -> None:
    '''Prints Go Fish title'''
    for line in const.GO_FISH_TITLE:
        print(line)

def get_player_name() -> str:
    '''Prompts input and returns user's name'''
    validate = ''
    while validate.lower() != 'y':
        human_name = input('Please enter name: ').title()
        validate = input('Confirm name? (y/n) "' + human_name + '": ')
    print('\nWelcome ' + human_name + '!')
    print()
    return human_name

def draw_board(players:list[Player], show_all_hands=False) -> None:
    '''Prints each player's hand, showing only the human player's cards'''
    for player in players:
        if not show_all_hands and player.bot():
            player.print_hidden_hand()
        else:
            player.print_visible_hand()

def end_scene() -> None:
    '''Prompts user for ENTER key and prints newlines'''
    input('Press ENTER to continue...')
    print('\n' * 6)

def pick_player(active_player:Player, all_players:list[Player]) -> Player:
    '''Prompts user for player and returns player'''
    choosable_players = [player for player in all_players if player.name() != active_player.name()]

    if active_player.bot():
        return random.choice(choosable_players)

    is_player_selected = False
    picked_player = None
    player_name = input(active_player.name() + ', select a player: ').title()
    while not is_player_selected:
        for player in choosable_players:
            if player.name() == player_name:
                picked_player = player
                is_player_selected = True
                break
        if not is_player_selected:
            player_name = input(player_name + ' is not another player. Try again: ').title()

    return picked_player

def pick_card(active_player:Player) -> Card:
    '''Prompts user for card and returns card'''
    if active_player.bot():
        return random.choice(active_player.hand())

    is_card_selected = False
    picked_card = None
    card_face = input(
        active_player.name() + ', select a card from your hand (2-10, J, Q, K, or A): ').title()
    while not is_card_selected:
        for card in active_player.hand():
            if card.face() == card_face:
                picked_card = card
                is_card_selected = True
                break
        if not is_card_selected:
            card_face = input(card_face + ' is not a card in your hand. Try again: ').title()
    print()

    return picked_card

def print_dialogue(active_player:Player, picked_player:Player,
                   picked_card:Card, is_picked_card_in_hand:bool) -> None:
    '''Prints dialogue after turn'''
    print(active_player.name() + ': ' +
          picked_player.name() + ', do you have any ' + picked_card.face() + '\'s?')
    print(picked_player.name() + ': ', end='')
    if is_picked_card_in_hand:
        print('Yes, I do.')
    else:
        print('No. Go fish!')

    print()

def announce_win(player:Player) -> None:
    '''Prints player win'''
    print(player.name(), 'wins!')

def announce_draw() -> None:
    '''Prints game drawn'''
    print('Draw! (No more cards in the deck)')
