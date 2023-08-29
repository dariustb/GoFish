''' app.py - Driver file for the application '''

# pylint: disable=C0103

from py.player import Player
from py.deck   import Deck
from py.card   import Card
from py import board
from py import constants as const

if __name__ == '__main__':
    # Print title
    board.print_title()

    # Set up bot players
    GamePlayers = [Player(name) for name in const.PLAYER_NAMES]

    # Set up human player
    human_name = board.get_player_name()
    GamePlayers.append(Player(name=human_name, bot=False))

    # Set up deck + deal cards to each player
    GameDeck = Deck()
    for player in GamePlayers:
        for _ in range(const.CARDS_IN_HAND):
            player.draw_card(GameDeck)

    # Show hand at beginning of game
    board.draw_board(GamePlayers)

    # Throw out all pairs in each player's hand
    for player in GamePlayers:
        player.toss_all_card_pairs()
    board.end_scene()

    # Game loop
    is_game_over: bool = False
    active_idx: int = 0

    active_player: Player = None
    picked_player: Player = None
    picked_card:   str    = None
    is_picked_card_in_hand: bool = None
    tossed_card:   Card   = None

    while not is_game_over:
        # Print board
        board.draw_board(GamePlayers)

        # Select active player
        active_player = GamePlayers[active_idx]

        # Get player's choices (other player/card)
        picked_player = board.pick_player(active_player, GamePlayers)
        picked_card = board.pick_card(active_player)

        # Check if picked player's card exist in their hand
        is_picked_card_in_hand = picked_player.is_card_in_hand(picked_card.face())

        # Give dialogue of the turn
        board.print_dialogue(active_player, picked_player,
                                picked_card, is_picked_card_in_hand)

        # Take & match card/draw from deck
        if is_picked_card_in_hand:
            picked_player.give_player_card(active_player, picked_card)
            active_player.toss_card_pair(picked_card.face())
        else:
            active_player.draw_card(GameDeck)
            active_player.toss_card_pair()

        # Check if hand is empty / deck is empty
        is_game_over = (active_player.is_hand_empty() or
                        picked_player.is_hand_empty() or
                        GameDeck.is_empty())

        # Continue game
        board.end_scene()
        active_idx = (active_idx + 1) % const.NUM_OF_PLAYERS


    # Print final board
    board.draw_board(GamePlayers, show_all_hands=True)

    # Announce winner/draw
    if GameDeck.is_empty():
        board.announce_draw()
    elif active_player.is_hand_empty():
        board.announce_win(active_player)
    elif picked_player.is_hand_empty():
        board.announce_win(picked_player)
