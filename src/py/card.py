'''card.py - Card related class'''

class Card:
    '''Card identifying attr/functions'''
    def __init__(self, suit, face):
        self.d_suit: str = suit
        self.d_face: str = face
        self.d_space: str = '' if self.d_face == '10' else ' '

    # Getter Functions
    def suit(self) -> str:
        '''Getter for suit'''
        return self.d_suit

    def face(self) -> str:
        '''Getter for face'''
        return self.d_face

    def space(self) -> str:
        '''Getter for space'''
        return self.d_space
