from Meld import *


class HandInfo:
    on_first_draw = 0
    on_first_discard = 1

class Hand:
    def __init__(self, melds, hand_info=-1):
        self.melds = melds
        self.hand_info = hand_info

    def __str__(self):
        output = "Hand:\n"
        for meld in self.melds:
            output += "%s\n" % meld

        if self.hand_info is HandInfo.on_first_draw:
            output += "Hand Info: On first draw\n"
        elif self.hand_info is HandInfo.on_first_discard:
            output += "Hand Info: On first discard\n"

        return output


    def get_melds(self):
        return self.melds

    def get_hand_tiles(self):
        return [ x for sublist in self.melds for x in sublist ]

    def get_hand_info(self):
        return self.hand_info

    def has_hand_info(self):
        return not self.handInfo is -1

    def add_meld(self, meld):
        self.melds.append(meld)

    def compute_statistics(self):

        self.num_of_coins = 0
        self.num_of_bamboos = 0
        self.num_of_characters = 0
        self.num_of_winds = 0
        self.num_of_dragons = 0
        self.num_of_simples = 0
        self.num_of_terminals = 0
        self.num_of_chows = 0
        self.num_of_pungs = 0
        self.num_of_kongs = 0
        self.num_of_eyes = 0
        self.num_of_honnors = 0
        self.num_of_edges = 0
        self.num_of_honnors = 0
        self.num_of_suits = 0
        self.num_of_revealed = 0
        self.num_of_promoted = 0
        self.num_of_concealed = 0

        for meld in self.melds:

            # get meld stats
            self.num_of_coins += meld.num_of_coins
            self.num_of_bamboos += meld.num_of_bamboos
            self.num_of_characters += meld.num_of_characters
            self.num_of_winds += meld.num_of_winds
            self.num_of_dragons += meld.num_of_dragons
            self.num_of_terminals += meld.num_of_terminals
            self.num_of_simples += meld.num_of_simples
            self.num_of_honnors += meld.num_of_honnors
            self.num_of_edges += meld.num_of_edges
            self.num_of_honnors += meld.num_of_honnors
            self.num_of_suits += meld.num_of_suits

            # meld types
            if meld.type is MeldType.chow:
                self.num_of_chows += 1

            elif meld.type is MeldType.pung:
                self.num_of_pungs += 1

            elif meld.type is MeldType.kong:
                self.num_of_kongs += 1

            elif meld.type is MeldType.eyes:
                self.num_of_eyes += 1

            # meld statuses
            if meld.status is MeldStatus.revealed:
                self.num_of_revealed += 1
            elif meld.status is MeldStatus.promoted:
                self.num_of_promoted += 1
            elif meld.status is MeldStatus.concealed:
                self.num_of_concealed += 1





