from Tiles import *
from Utils import DotDict

class MeldStatus:
    open = 0
    concealed = 1
    promoted = 2

    reverse = [
        "open",
        "Concealed",
        "Promoted"
    ]

class MeldType:
    chow = 0
    pung = 1
    kong = 2
    eyes = 3

    reverse = [
        "Chow",
        "Pung",
        "Kong",
        "Eyes"
    ]


class Meld:
    def __init__(self, meld_status, meld_type, meld_tiles):
        self.status = meld_status
        self.type = meld_type
        self.tiles = meld_tiles
        self.compute_statistics()

    def get_tiles(self):
        return self.tiles


    def compute_statistics(self):

        self.num_of_coins = 0
        self.num_of_bamboos = 0
        self.num_of_characters = 0
        self.num_of_winds = 0
        self.num_of_dragons = 0
        self.num_of_simples = 0
        self.num_of_terminals = 0
        self.num_of_honnors = 0
        self.num_of_suits = 0
        self.num_of_edges = 0


        for tile in self.tiles:

            # Check Terminals
            if(tile.value is TileValue.one or
               tile.value is TileValue.nine):
                self.num_of_terminals += 1

            # Check Types
            if tile.type is TileType.coin :
                self.num_of_coins += 1
                self.num_of_simples += 1

            elif tile.type is TileType.bamboo:
                self.num_of_bamboos += 1

            elif tile.type is TileType.characters:
                self.num_of_characters += 1
                self.num_of_simples += 1

            elif(tile.type is TileType.east_wind or
                tile.type is TileType.south_wind or
                tile.type is TileType.west_wind or
                tile.type is TileType.north_wind):
                self.num_of_winds += 1

            elif(tile.type is TileType.red_dragon or
                tile.type is TileType.green_dragon or
                tile.type is TileType.white_dragon):
                self.num_of_dragons += 1

        self.num_of_edges = self.num_of_terminals + self.num_of_winds + self.num_of_dragons
        self.num_of_honnors = self.num_of_winds + self.num_of_dragons
        self.num_of_suits = self.num_of_coins + self.num_of_bamboos + self.num_of_characters






# Meld Collections

# Coins
coins_chow = DotDict()
coins_chow.o123 = Meld(MeldStatus.open, MeldType.chow, [c.t1, c.t2, c.t3])
coins_chow.o234 = Meld(MeldStatus.open, MeldType.chow, [c.t2, c.t3, c.t4])
coins_chow.o345 = Meld(MeldStatus.open, MeldType.chow, [c.t3, c.t4, c.t5])
coins_chow.o34r = Meld(MeldStatus.open, MeldType.chow, [c.t3, c.t4, c.tr])
coins_chow.o456 = Meld(MeldStatus.open, MeldType.chow, [c.t4, c.t5, c.t6])
coins_chow.o4r6 = Meld(MeldStatus.open, MeldType.chow, [c.t4, c.tr, c.t6])
coins_chow.o567 = Meld(MeldStatus.open, MeldType.chow, [c.t5, c.t6, c.t7])
coins_chow.or67 = Meld(MeldStatus.open, MeldType.chow, [c.tr, c.t6, c.t7])
coins_chow.o678 = Meld(MeldStatus.open, MeldType.chow, [c.t6, c.t7, c.t8])
coins_chow.o789 = Meld(MeldStatus.open, MeldType.chow, [c.t7, c.t8, c.t9])

coins_chow.c123 = Meld(MeldStatus.concealed, MeldType.chow, [c.t1, c.t2, c.t3])
coins_chow.c234 = Meld(MeldStatus.concealed, MeldType.chow, [c.t2, c.t3, c.t4])
coins_chow.c345 = Meld(MeldStatus.concealed, MeldType.chow, [c.t3, c.t4, c.t5])
coins_chow.c34r = Meld(MeldStatus.concealed, MeldType.chow, [c.t3, c.t4, c.tr])
coins_chow.c456 = Meld(MeldStatus.concealed, MeldType.chow, [c.t4, c.t5, c.t6])
coins_chow.c4r6 = Meld(MeldStatus.concealed, MeldType.chow, [c.t4, c.tr, c.t6])
coins_chow.c567 = Meld(MeldStatus.concealed, MeldType.chow, [c.t5, c.t6, c.t7])
coins_chow.cr67 = Meld(MeldStatus.concealed, MeldType.chow, [c.tr, c.t6, c.t7])
coins_chow.c678 = Meld(MeldStatus.concealed, MeldType.chow, [c.t6, c.t7, c.t8])
coins_chow.c789 = Meld(MeldStatus.concealed, MeldType.chow, [c.t7, c.t8, c.t9])

coins_pung = DotDict()
coins_pung.o111 = Meld(MeldStatus.open, MeldType.pung, [c.t1, c.t1, c.t1])
coins_pung.o222 = Meld(MeldStatus.open, MeldType.pung, [c.t2, c.t2, c.t2])
coins_pung.o333 = Meld(MeldStatus.open, MeldType.pung, [c.t3, c.t3, c.t3])
coins_pung.o444 = Meld(MeldStatus.open, MeldType.pung, [c.t4, c.t4, c.t4])
coins_pung.o555 = Meld(MeldStatus.open, MeldType.pung, [c.t5, c.t5, c.t5])
coins_pung.or55 = Meld(MeldStatus.open, MeldType.pung, [c.tr, c.t5, c.t5])
coins_pung.o5r5 = Meld(MeldStatus.open, MeldType.pung, [c.t5, c.tr, c.t5])
coins_pung.o55r = Meld(MeldStatus.open, MeldType.pung, [c.t5, c.t5, c.tr])
coins_pung.o666 = Meld(MeldStatus.open, MeldType.pung, [c.t6, c.t6, c.t6])
coins_pung.o777 = Meld(MeldStatus.open, MeldType.pung, [c.t7, c.t7, c.t7])
coins_pung.o888 = Meld(MeldStatus.open, MeldType.pung, [c.t8, c.t8, c.t8])
coins_pung.o999 = Meld(MeldStatus.open, MeldType.pung, [c.t9, c.t9, c.t9])

coins_pung.c111 = Meld(MeldStatus.concealed, MeldType.pung, [c.t1, c.t1, c.t1])
coins_pung.c222 = Meld(MeldStatus.concealed, MeldType.pung, [c.t2, c.t2, c.t2])
coins_pung.c333 = Meld(MeldStatus.concealed, MeldType.pung, [c.t3, c.t3, c.t3])
coins_pung.c444 = Meld(MeldStatus.concealed, MeldType.pung, [c.t4, c.t4, c.t4])
coins_pung.c555 = Meld(MeldStatus.concealed, MeldType.pung, [c.t5, c.t5, c.t5])
coins_pung.cr55 = Meld(MeldStatus.concealed, MeldType.pung, [c.tr, c.t5, c.t5])
coins_pung.c5r5 = Meld(MeldStatus.concealed, MeldType.pung, [c.t5, c.tr, c.t5])
coins_pung.c55r = Meld(MeldStatus.concealed, MeldType.pung, [c.t5, c.t5, c.tr])
coins_pung.c666 = Meld(MeldStatus.concealed, MeldType.pung, [c.t6, c.t6, c.t6])
coins_pung.c777 = Meld(MeldStatus.concealed, MeldType.pung, [c.t7, c.t7, c.t7])
coins_pung.c888 = Meld(MeldStatus.concealed, MeldType.pung, [c.t8, c.t8, c.t8])
coins_pung.c999 = Meld(MeldStatus.concealed, MeldType.pung, [c.t9, c.t9, c.t9])

coins_kong = DotDict()
coins_kong.o1111 = Meld(MeldStatus.open, MeldType.kong, [c.t1, c.t1, c.t1, c.t1])
coins_kong.o2222 = Meld(MeldStatus.open, MeldType.kong, [c.t2, c.t2, c.t2, c.t2])
coins_kong.o3333 = Meld(MeldStatus.open, MeldType.kong, [c.t3, c.t3, c.t3, c.t3])
coins_kong.o4444 = Meld(MeldStatus.open, MeldType.kong, [c.t4, c.t4, c.t4, c.t4])
coins_kong.o5555 = Meld(MeldStatus.open, MeldType.kong, [c.t5, c.t5, c.t5, c.t5])
coins_kong.or555 = Meld(MeldStatus.open, MeldType.kong, [c.tr, c.t5, c.t5, c.t5])
coins_kong.o5r55 = Meld(MeldStatus.open, MeldType.kong, [c.t5, c.tr, c.t5, c.t5])
coins_kong.o55r5 = Meld(MeldStatus.open, MeldType.kong, [c.t5, c.t5, c.tr, c.t5])
coins_kong.or55r = Meld(MeldStatus.open, MeldType.kong, [c.tr, c.t5, c.t5, c.tr])
coins_kong.o6666 = Meld(MeldStatus.open, MeldType.kong, [c.t6, c.t6, c.t6, c.t6])
coins_kong.o7777 = Meld(MeldStatus.open, MeldType.kong, [c.t7, c.t7, c.t7, c.t7])
coins_kong.o8888 = Meld(MeldStatus.open, MeldType.kong, [c.t8, c.t8, c.t8, c.t8])
coins_kong.o9999 = Meld(MeldStatus.open, MeldType.kong, [c.t9, c.t9, c.t9, c.t9])

coins_kong.c1111 = Meld(MeldStatus.concealed, MeldType.kong, [c.t1, c.t1, c.t1, c.t1])
coins_kong.c2222 = Meld(MeldStatus.concealed, MeldType.kong, [c.t2, c.t2, c.t2, c.t2])
coins_kong.c3333 = Meld(MeldStatus.concealed, MeldType.kong, [c.t3, c.t3, c.t3, c.t3])
coins_kong.c4444 = Meld(MeldStatus.concealed, MeldType.kong, [c.t4, c.t4, c.t4, c.t4])
coins_kong.c5555 = Meld(MeldStatus.concealed, MeldType.kong, [c.t5, c.t5, c.t5, c.t5])
coins_kong.cr555 = Meld(MeldStatus.concealed, MeldType.kong, [c.tr, c.t5, c.t5, c.t5])
coins_kong.c5r55 = Meld(MeldStatus.concealed, MeldType.kong, [c.t5, c.tr, c.t5, c.t5])
coins_kong.c55r5 = Meld(MeldStatus.concealed, MeldType.kong, [c.t5, c.t5, c.tr, c.t5])
coins_kong.cr55r = Meld(MeldStatus.concealed, MeldType.kong, [c.tr, c.t5, c.t5, c.tr])
coins_kong.c6666 = Meld(MeldStatus.concealed, MeldType.kong, [c.t6, c.t6, c.t6, c.t6])
coins_kong.c7777 = Meld(MeldStatus.concealed, MeldType.kong, [c.t7, c.t7, c.t7, c.t7])
coins_kong.c8888 = Meld(MeldStatus.concealed, MeldType.kong, [c.t8, c.t8, c.t8, c.t8])
coins_kong.c9999 = Meld(MeldStatus.concealed, MeldType.kong, [c.t9, c.t9, c.t9, c.t9])

coins_eyes = DotDict()
coins_eyes.o11 = Meld(MeldStatus.open, MeldType.eyes, [c.t1, c.t1])
coins_eyes.o22 = Meld(MeldStatus.open, MeldType.eyes, [c.t2, c.t2])
coins_eyes.o33 = Meld(MeldStatus.open, MeldType.eyes, [c.t3, c.t3])
coins_eyes.o44 = Meld(MeldStatus.open, MeldType.eyes, [c.t4, c.t4])
coins_eyes.o55 = Meld(MeldStatus.open, MeldType.eyes, [c.t5, c.t5])
coins_eyes.or5 = Meld(MeldStatus.open, MeldType.eyes, [c.tr, c.t5])
coins_eyes.o5r = Meld(MeldStatus.open, MeldType.eyes, [c.t5, c.tr])
coins_eyes.o66 = Meld(MeldStatus.open, MeldType.eyes, [c.t6, c.t6])
coins_eyes.o77 = Meld(MeldStatus.open, MeldType.eyes, [c.t7, c.t7])
coins_eyes.o88 = Meld(MeldStatus.open, MeldType.eyes, [c.t8, c.t8])
coins_eyes.o99 = Meld(MeldStatus.open, MeldType.eyes, [c.t9, c.t9])

coins_eyes.c11 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t1, c.t1])
coins_eyes.c22 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t2, c.t2])
coins_eyes.c33 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t3, c.t3])
coins_eyes.c44 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t4, c.t4])
coins_eyes.c55 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t5, c.t5])
coins_eyes.cr5 = Meld(MeldStatus.concealed, MeldType.eyes, [c.tr, c.t5])
coins_eyes.c5r = Meld(MeldStatus.concealed, MeldType.eyes, [c.t5, c.tr])
coins_eyes.c66 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t6, c.t6])
coins_eyes.c77 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t7, c.t7])
coins_eyes.c88 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t8, c.t8])
coins_eyes.c99 = Meld(MeldStatus.concealed, MeldType.eyes, [c.t9, c.t9])


# Bamboos
bamboo_chow = DotDict()
bamboo_chow.o123 = Meld(MeldStatus.open, MeldType.chow, [b.t1, b.t2, b.t3])
bamboo_chow.o234 = Meld(MeldStatus.open, MeldType.chow, [b.t2, b.t3, b.t4])
bamboo_chow.o345 = Meld(MeldStatus.open, MeldType.chow, [b.t3, b.t4, b.t5])
bamboo_chow.o34r = Meld(MeldStatus.open, MeldType.chow, [b.t3, b.t4, b.tr])
bamboo_chow.o456 = Meld(MeldStatus.open, MeldType.chow, [b.t4, b.t5, b.t6])
bamboo_chow.o4r6 = Meld(MeldStatus.open, MeldType.chow, [b.t4, b.tr, b.t6])
bamboo_chow.o567 = Meld(MeldStatus.open, MeldType.chow, [b.t5, b.t6, b.t7])
bamboo_chow.or67 = Meld(MeldStatus.open, MeldType.chow, [b.tr, b.t6, b.t7])
bamboo_chow.o678 = Meld(MeldStatus.open, MeldType.chow, [b.t6, b.t7, b.t8])
bamboo_chow.o789 = Meld(MeldStatus.open, MeldType.chow, [b.t7, b.t8, b.t9])

bamboo_chow.c123 = Meld(MeldStatus.concealed, MeldType.chow, [b.t1, b.t2, b.t3])
bamboo_chow.c234 = Meld(MeldStatus.concealed, MeldType.chow, [b.t2, b.t3, b.t4])
bamboo_chow.c345 = Meld(MeldStatus.concealed, MeldType.chow, [b.t3, b.t4, b.t5])
bamboo_chow.c34r = Meld(MeldStatus.concealed, MeldType.chow, [b.t3, b.t4, b.tr])
bamboo_chow.c456 = Meld(MeldStatus.concealed, MeldType.chow, [b.t4, b.t5, b.t6])
bamboo_chow.c4r6 = Meld(MeldStatus.concealed, MeldType.chow, [b.t4, b.tr, b.t6])
bamboo_chow.c567 = Meld(MeldStatus.concealed, MeldType.chow, [b.t5, b.t6, b.t7])
bamboo_chow.cr67 = Meld(MeldStatus.concealed, MeldType.chow, [b.tr, b.t6, b.t7])
bamboo_chow.c678 = Meld(MeldStatus.concealed, MeldType.chow, [b.t6, b.t7, b.t8])
bamboo_chow.c789 = Meld(MeldStatus.concealed, MeldType.chow, [b.t7, b.t8, b.t9])

bamboo_pung = DotDict()
bamboo_pung.o111 = Meld(MeldStatus.open, MeldType.pung, [b.t1, b.t1, b.t1])
bamboo_pung.o222 = Meld(MeldStatus.open, MeldType.pung, [b.t2, b.t2, b.t2])
bamboo_pung.o333 = Meld(MeldStatus.open, MeldType.pung, [b.t3, b.t3, b.t3])
bamboo_pung.o444 = Meld(MeldStatus.open, MeldType.pung, [b.t4, b.t4, b.t4])
bamboo_pung.o555 = Meld(MeldStatus.open, MeldType.pung, [b.t5, b.t5, b.t5])
bamboo_pung.or55 = Meld(MeldStatus.open, MeldType.pung, [b.tr, b.t5, b.t5])
bamboo_pung.o5r5 = Meld(MeldStatus.open, MeldType.pung, [b.t5, b.tr, b.t5])
bamboo_pung.o55r = Meld(MeldStatus.open, MeldType.pung, [b.t5, b.t5, b.tr])
bamboo_pung.o666 = Meld(MeldStatus.open, MeldType.pung, [b.t6, b.t6, b.t6])
bamboo_pung.o777 = Meld(MeldStatus.open, MeldType.pung, [b.t7, b.t7, b.t7])
bamboo_pung.o888 = Meld(MeldStatus.open, MeldType.pung, [b.t8, b.t8, b.t8])
bamboo_pung.o999 = Meld(MeldStatus.open, MeldType.pung, [b.t9, b.t9, b.t9])

bamboo_pung.c111 = Meld(MeldStatus.concealed, MeldType.pung, [b.t1, b.t1, b.t1])
bamboo_pung.c222 = Meld(MeldStatus.concealed, MeldType.pung, [b.t2, b.t2, b.t2])
bamboo_pung.c333 = Meld(MeldStatus.concealed, MeldType.pung, [b.t3, b.t3, b.t3])
bamboo_pung.c444 = Meld(MeldStatus.concealed, MeldType.pung, [b.t4, b.t4, b.t4])
bamboo_pung.c555 = Meld(MeldStatus.concealed, MeldType.pung, [b.t5, b.t5, b.t5])
bamboo_pung.cr55 = Meld(MeldStatus.concealed, MeldType.pung, [b.tr, b.t5, b.t5])
bamboo_pung.c5r5 = Meld(MeldStatus.concealed, MeldType.pung, [b.t5, b.tr, b.t5])
bamboo_pung.c55r = Meld(MeldStatus.concealed, MeldType.pung, [b.t5, b.t5, b.tr])
bamboo_pung.c666 = Meld(MeldStatus.concealed, MeldType.pung, [b.t6, b.t6, b.t6])
bamboo_pung.c777 = Meld(MeldStatus.concealed, MeldType.pung, [b.t7, b.t7, b.t7])
bamboo_pung.c888 = Meld(MeldStatus.concealed, MeldType.pung, [b.t8, b.t8, b.t8])
bamboo_pung.c999 = Meld(MeldStatus.concealed, MeldType.pung, [b.t9, b.t9, b.t9])

bamboo_kong = DotDict()
bamboo_kong.o1111 = Meld(MeldStatus.open, MeldType.kong, [b.t1, b.t1, b.t1, b.t1])
bamboo_kong.o2222 = Meld(MeldStatus.open, MeldType.kong, [b.t2, b.t2, b.t2, b.t2])
bamboo_kong.o3333 = Meld(MeldStatus.open, MeldType.kong, [b.t3, b.t3, b.t3, b.t3])
bamboo_kong.o4444 = Meld(MeldStatus.open, MeldType.kong, [b.t4, b.t4, b.t4, b.t4])
bamboo_kong.o5555 = Meld(MeldStatus.open, MeldType.kong, [b.t5, b.t5, b.t5, b.t5])
bamboo_kong.or555 = Meld(MeldStatus.open, MeldType.kong, [b.tr, b.t5, b.t5, b.t5])
bamboo_kong.o5r55 = Meld(MeldStatus.open, MeldType.kong, [b.t5, b.tr, b.t5, b.t5])
bamboo_kong.o55r5 = Meld(MeldStatus.open, MeldType.kong, [b.t5, b.t5, b.tr, b.t5])
bamboo_kong.o555r = Meld(MeldStatus.open, MeldType.kong, [b.t5, b.t5, b.t5, b.tr])
bamboo_kong.o6666 = Meld(MeldStatus.open, MeldType.kong, [b.t6, b.t6, b.t6, b.t6])
bamboo_kong.o7777 = Meld(MeldStatus.open, MeldType.kong, [b.t7, b.t7, b.t7, b.t7])
bamboo_kong.o8888 = Meld(MeldStatus.open, MeldType.kong, [b.t8, b.t8, b.t8, b.t8])
bamboo_kong.o9999 = Meld(MeldStatus.open, MeldType.kong, [b.t9, b.t9, b.t9, b.t9])

bamboo_kong.c1111 = Meld(MeldStatus.concealed, MeldType.kong, [b.t1, b.t1, b.t1, b.t1])
bamboo_kong.c2222 = Meld(MeldStatus.concealed, MeldType.kong, [b.t2, b.t2, b.t2, b.t2])
bamboo_kong.c3333 = Meld(MeldStatus.concealed, MeldType.kong, [b.t3, b.t3, b.t3, b.t3])
bamboo_kong.c4444 = Meld(MeldStatus.concealed, MeldType.kong, [b.t4, b.t4, b.t4, b.t4])
bamboo_kong.c5555 = Meld(MeldStatus.concealed, MeldType.kong, [b.t5, b.t5, b.t5, b.t5])
bamboo_kong.cr555 = Meld(MeldStatus.concealed, MeldType.kong, [b.tr, b.t5, b.t5, b.t5])
bamboo_kong.c5r55 = Meld(MeldStatus.concealed, MeldType.kong, [b.t5, b.tr, b.t5, b.t5])
bamboo_kong.c55r5 = Meld(MeldStatus.concealed, MeldType.kong, [b.t5, b.t5, b.tr, b.t5])
bamboo_kong.c555r = Meld(MeldStatus.concealed, MeldType.kong, [b.t5, b.t5, b.t5, b.tr])
bamboo_kong.c6666 = Meld(MeldStatus.concealed, MeldType.kong, [b.t6, b.t6, b.t6, b.t6])
bamboo_kong.c7777 = Meld(MeldStatus.concealed, MeldType.kong, [b.t7, b.t7, b.t7, b.t7])
bamboo_kong.c8888 = Meld(MeldStatus.concealed, MeldType.kong, [b.t8, b.t8, b.t8, b.t8])
bamboo_kong.c9999 = Meld(MeldStatus.concealed, MeldType.kong, [b.t9, b.t9, b.t9, b.t9])

bamboo_eyes = DotDict()
bamboo_eyes.o11 = meld(meldstatus.open, meldtype.eyes, [b.t1, b.t1])
bamboo_eyes.o22 = meld(meldstatus.open, meldtype.eyes, [b.t2, b.t2])
bamboo_eyes.o33 = meld(meldstatus.open, meldtype.eyes, [b.t3, b.t3])
bamboo_eyes.o44 = meld(meldstatus.open, meldtype.eyes, [b.t4, b.t4])
bamboo_eyes.o55 = meld(meldstatus.open, meldtype.eyes, [b.t5, b.t5])
bamboo_eyes.or5 = meld(meldstatus.open, meldtype.eyes, [b.tr, b.t5])
bamboo_eyes.o5r = meld(meldstatus.open, meldtype.eyes, [b.t5, b.tr])
bamboo_eyes.o66 = meld(meldstatus.open, meldtype.eyes, [b.t6, b.t6])
bamboo_eyes.o77 = meld(meldstatus.open, meldtype.eyes, [b.t7, b.t7])
bamboo_eyes.o88 = meld(meldstatus.open, meldtype.eyes, [b.t8, b.t8])
bamboo_eyes.o99 = meld(meldstatus.open, meldtype.eyes, [b.t9, b.t9])

bamboo_eyes.c11 = meld(meldstatus.concealed, meldtype.eyes, [b.t1, b.t1])
bamboo_eyes.c22 = meld(meldstatus.concealed, meldtype.eyes, [b.t2, b.t2])
bamboo_eyes.c33 = meld(meldstatus.concealed, meldtype.eyes, [b.t3, b.t3])
bamboo_eyes.c44 = meld(meldstatus.concealed, meldtype.eyes, [b.t4, b.t4])
bamboo_eyes.c55 = meld(meldstatus.concealed, meldtype.eyes, [b.t5, b.t5])
bamboo_eyes.cr5 = meld(meldstatus.concealed, meldtype.eyes, [b.tr, b.t5])
bamboo_eyes.c5r = meld(meldstatus.concealed, meldtype.eyes, [b.t5, b.tr])
bamboo_eyes.c66 = meld(meldstatus.concealed, meldtype.eyes, [b.t6, b.t6])
bamboo_eyes.c77 = meld(meldstatus.concealed, meldtype.eyes, [b.t7, b.t7])
bamboo_eyes.c88 = meld(meldstatus.concealed, meldtype.eyes, [b.t8, b.t8])
bamboo_eyes.c99 = meld(meldstatus.concealed, meldtype.eyes, [b.t9, b.t9])


# Characters
character_chows = DotDict()
character_chows.o123 = Meld(MeldStatus.open, MeldType.chow, [k.t1, k.t2, k.t3])
character_chows.o234 = Meld(MeldStatus.open, MeldType.chow, [k.t2, k.t3, k.t4])
character_chows.o345 = Meld(MeldStatus.open, MeldType.chow, [k.t3, k.t4, k.t5])
character_chows.o34r = Meld(MeldStatus.open, MeldType.chow, [k.t3, k.t4, k.tr])
character_chows.o456 = Meld(MeldStatus.open, MeldType.chow, [k.t4, k.t5, k.t6])
character_chows.o4r6 = Meld(MeldStatus.open, MeldType.chow, [k.t4, k.tr, k.t6])
character_chows.o567 = Meld(MeldStatus.open, MeldType.chow, [k.t5, k.t6, k.t7])
character_chows.or67 = Meld(MeldStatus.open, MeldType.chow, [k.tr, k.t6, k.t7])
character_chows.o678 = Meld(MeldStatus.open, MeldType.chow, [k.t6, k.t7, k.t8])
character_chows.o789 = Meld(MeldStatus.open, MeldType.chow, [k.t7, k.t8, k.t9])

character_chows.c123 = Meld(MeldStatus.concealed, MeldType.chow, [k.t1, k.t2, k.t3])
character_chows.c234 = Meld(MeldStatus.concealed, MeldType.chow, [k.t2, k.t3, k.t4])
character_chows.c345 = Meld(MeldStatus.concealed, MeldType.chow, [k.t3, k.t4, k.t5])
character_chows.c34r = Meld(MeldStatus.concealed, MeldType.chow, [k.t3, k.t4, k.tr])
character_chows.c456 = Meld(MeldStatus.concealed, MeldType.chow, [k.t4, k.t5, k.t6])
character_chows.c4r6 = Meld(MeldStatus.concealed, MeldType.chow, [k.t4, k.tr, k.t6])
character_chows.c567 = Meld(MeldStatus.concealed, MeldType.chow, [k.t5, k.t6, k.t7])
character_chows.cr67 = Meld(MeldStatus.concealed, MeldType.chow, [k.tr, k.t6, k.t7])
character_chows.c678 = Meld(MeldStatus.concealed, MeldType.chow, [k.t6, k.t7, k.t8])
character_chows.c789 = Meld(MeldStatus.concealed, MeldType.chow, [k.t7, k.t8, k.t9])


character_pungs = DotDict()
character_pungs.o111 = Meld(MeldStatus.opwn, MeldType.pung, [k.t1, k.t1, k.t1])
character_pungs.o222 = Meld(MeldStatus.opwn, MeldType.pung, [k.t2, k.t2, k.t2])
character_pungs.o333 = Meld(MeldStatus.opwn, MeldType.pung, [k.t3, k.t3, k.t3])
character_pungs.o444 = Meld(MeldStatus.opwn, MeldType.pung, [k.t4, k.t4, k.t4])
character_pungs.o555 = Meld(MeldStatus.opwn, MeldType.pung, [k.t5, k.t5, k.t5])
character_pungs.or55 = Meld(MeldStatus.opwn, MeldType.pung, [k.tr, k.t5, k.t5])
character_pungs.o5r5 = Meld(MeldStatus.opwn, MeldType.pung, [k.t5, k.tr, k.t5])
character_pungs.o55r = Meld(MeldStatus.opwn, MeldType.pung, [k.t5, k.t5, k.tr])
character_pungs.o666 = Meld(MeldStatus.opwn, MeldType.pung, [k.t6, k.t6, k.t6])
character_pungs.o777 = Meld(MeldStatus.opwn, MeldType.pung, [k.t7, k.t7, k.t7])
character_pungs.o888 = Meld(MeldStatus.opwn, MeldType.pung, [k.t8, k.t8, k.t8])
character_pungs.o999 = Meld(MeldStatus.opwn, MeldType.pung, [k.t9, k.t9, k.t9])

character_pungs.c111 = Meld(MeldStatus.concealed, MeldType.pung, [k.t1, k.t1, k.t1])
character_pungs.c222 = Meld(MeldStatus.concealed, MeldType.pung, [k.t2, k.t2, k.t2])
character_pungs.c333 = Meld(MeldStatus.concealed, MeldType.pung, [k.t3, k.t3, k.t3])
character_pungs.c444 = Meld(MeldStatus.concealed, MeldType.pung, [k.t4, k.t4, k.t4])
character_pungs.c555 = Meld(MeldStatus.concealed, MeldType.pung, [k.t5, k.t5, k.t5])
character_pungs.cr55 = Meld(MeldStatus.concealed, MeldType.pung, [k.tr, k.t5, k.t5])
character_pungs.c5r5 = Meld(MeldStatus.concealed, MeldType.pung, [k.t5, k.tr, k.t5])
character_pungs.c55r = Meld(MeldStatus.concealed, MeldType.pung, [k.t5, k.t5, k.tr])
character_pungs.c666 = Meld(MeldStatus.concealed, MeldType.pung, [k.t6, k.t6, k.t6])
character_pungs.c777 = Meld(MeldStatus.concealed, MeldType.pung, [k.t7, k.t7, k.t7])
character_pungs.c888 = Meld(MeldStatus.concealed, MeldType.pung, [k.t8, k.t8, k.t8])
character_pungs.c999 = Meld(MeldStatus.concealed, MeldType.pung, [k.t9, k.t9, k.t9])


character_kongs = DotDict()
character_kongs.o1111 = Meld(MeldStatus.open, MeldType.kong, [k.t1, k.t1, k.t1, k.t1])
character_kongs.o2222 = Meld(MeldStatus.open, MeldType.kong, [k.t2, k.t2, k.t2, k.t2])
character_kongs.o3333 = Meld(MeldStatus.open, MeldType.kong, [k.t3, k.t3, k.t3, k.t3])
character_kongs.o4444 = Meld(MeldStatus.open, MeldType.kong, [k.t4, k.t4, k.t4, k.t4])
character_kongs.o5555 = Meld(MeldStatus.open, MeldType.kong, [k.t5, k.t5, k.t5, k.t5])
character_kongs.or555 = Meld(MeldStatus.open, MeldType.kong, [k.tr, k.t5, k.t5, k.t5])
character_kongs.o5r55 = Meld(MeldStatus.open, MeldType.kong, [k.t5, k.tr, k.t5, k.t5])
character_kongs.o55r5 = Meld(MeldStatus.open, MeldType.kong, [k.t5, k.t5, k.tr, k.t5])
character_kongs.o555r = Meld(MeldStatus.open, MeldType.kong, [k.t5, k.t5, k.t5, k.tr])
character_kongs.o6666 = Meld(MeldStatus.open, MeldType.kong, [k.t6, k.t6, k.t6, k.t6])
character_kongs.o7777 = Meld(MeldStatus.open, MeldType.kong, [k.t7, k.t7, k.t7, k.t7])
character_kongs.o8888 = Meld(MeldStatus.open, MeldType.kong, [k.t8, k.t8, k.t8, k.t8])
character_kongs.o9999 = Meld(MeldStatus.open, MeldType.kong, [k.t9, k.t9, k.t9, k.t9])

character_kongs.c1111 = Meld(MeldStatus.concealed, MeldType.kong, [k.t1, k.t1, k.t1, k.t1])
character_kongs.c2222 = Meld(MeldStatus.concealed, MeldType.kong, [k.t2, k.t2, k.t2, k.t2])
character_kongs.c3333 = Meld(MeldStatus.concealed, MeldType.kong, [k.t3, k.t3, k.t3, k.t3])
character_kongs.c4444 = Meld(MeldStatus.concealed, MeldType.kong, [k.t4, k.t4, k.t4, k.t4])
character_kongs.c5555 = Meld(MeldStatus.concealed, MeldType.kong, [k.t5, k.t5, k.t5, k.t5])
character_kongs.cr555 = Meld(MeldStatus.concealed, MeldType.kong, [k.tr, k.t5, k.t5, k.t5])
character_kongs.c5r55 = Meld(MeldStatus.concealed, MeldType.kong, [k.t5, k.tr, k.t5, k.t5])
character_kongs.c55r5 = Meld(MeldStatus.concealed, MeldType.kong, [k.t5, k.t5, k.tr, k.t5])
character_kongs.c555r = Meld(MeldStatus.concealed, MeldType.kong, [k.t5, k.t5, k.t5, k.tr])
character_kongs.c6666 = Meld(MeldStatus.concealed, MeldType.kong, [k.t6, k.t6, k.t6, k.t6])
character_kongs.c7777 = Meld(MeldStatus.concealed, MeldType.kong, [k.t7, k.t7, k.t7, k.t7])
character_kongs.c8888 = Meld(MeldStatus.concealed, MeldType.kong, [k.t8, k.t8, k.t8, k.t8])
character_kongs.c9999 = Meld(MeldStatus.concealed, MeldType.kong, [k.t9, k.t9, k.t9, k.t9])


character_eyes = DotDict()
character_eyes.o11 = Meld(MeldStatus.open, MeldType.eyes, [k.t1, k.t1])
character_eyes.o22 = Meld(MeldStatus.open, MeldType.eyes, [k.t2, k.t2])
character_eyes.o33 = Meld(MeldStatus.open, MeldType.eyes, [k.t3, k.t3])
character_eyes.o44 = Meld(MeldStatus.open, MeldType.eyes, [k.t4, k.t4])
character_eyes.o55 = Meld(MeldStatus.open, MeldType.eyes, [k.t5, k.t5])
character_eyes.or5 = Meld(MeldStatus.open, MeldType.eyes, [k.tr, k.t5])
character_eyes.o5r = Meld(MeldStatus.open, MeldType.eyes, [k.t5, k.tr])
character_eyes.o66 = Meld(MeldStatus.open, MeldType.eyes, [k.t6, k.t6])
character_eyes.o77 = Meld(MeldStatus.open, MeldType.eyes, [k.t7, k.t7])
character_eyes.o88 = Meld(MeldStatus.open, MeldType.eyes, [k.t8, k.t8])
character_eyes.o99 = Meld(MeldStatus.open, MeldType.eyes, [k.t9, k.t9])

character_eyes.c11 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t1, k.t1])
character_eyes.c22 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t2, k.t2])
character_eyes.c33 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t3, k.t3])
character_eyes.c44 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t4, k.t4])
character_eyes.c55 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t5, k.t5])
character_eyes.cr5 = Meld(MeldStatus.concealed, MeldType.eyes, [k.tr, k.t5])
character_eyes.c5r = Meld(MeldStatus.concealed, MeldType.eyes, [k.t5, k.tr])
character_eyes.c66 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t6, k.t6])
character_eyes.c77 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t7, k.t7])
character_eyes.c88 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t8, k.t8])
character_eyes.c99 = Meld(MeldStatus.concealed, MeldType.eyes, [k.t9, k.t9])

# Winds

wind_pungs = DotDict()
wind_pungs.oeee = Meld(MeldStatus.open, MeldType.pung, [w.e, w.e, w.e])
wind_pungs.osss = Meld(MeldStatus.open, MeldType.pung, [w.s, w.s, w.s])
wind_pungs.owww = Meld(MeldStatus.open, MeldType.pung, [w.w, w.w, w.w])
wind_pungs.onnn = Meld(MeldStatus.open, MeldType.pung, [w.n, w.n, w.n])

wind_pungs.ceee = Meld(MeldStatus.concealed, MeldType.pung, [w.e, w.e, w.e])
wind_pungs.csss = Meld(MeldStatus.concealed, MeldType.pung, [w.s, w.s, w.s])
wind_pungs.cwww = Meld(MeldStatus.concealed, MeldType.pung, [w.w, w.w, w.w])
wind_pungs.cnnn = Meld(MeldStatus.concealed, MeldType.pung, [w.n, w.n, w.n])

wind_kongs = DotDict()
wind_kings.oeeee = Meld(MeldStatus.open, MeldType.kong, [w.e, w.e, w.e, w.e])
wind_kings.ossss = Meld(MeldStatus.open, MeldType.kong, [w.s, w.s, w.s, w.s])
wind_kings.owwww = Meld(MeldStatus.open, MeldType.kong, [w.w, w.w, w.w, w.w])
wind_kings.onnnn = Meld(MeldStatus.open, MeldType.kong, [w.n, w.n, w.n, w.n])

wind_kings.ceeee = Meld(MeldStatus.concealed, MeldType.kong, [w.e, w.e, w.e, w.e])
wind_kings.cssss = Meld(MeldStatus.concealed, MeldType.kong, [w.s, w.s, w.s, w.s])
wind_kings.cwwww = Meld(MeldStatus.concealed, MeldType.kong, [w.w, w.w, w.w, w.w])
wind_kings.cnnnn = Meld(MeldStatus.concealed, MeldType.kong, [w.n, w.n, w.n, w.n])


wind_eyes = DotDict()
wind_eyes.oee = Meld(MeldStatus.open, MeldType.eyes, [w.e, w.e])
wind_eyes.oss = Meld(MeldStatus.open, MeldType.eyes, [w.s, w.s])
wind_eyes.oww = Meld(MeldStatus.open, MeldType.eyes, [w.w, w.w])
wind_eyes.onn = Meld(MeldStatus.open, MeldType.eyes, [w.n, w.n])

wind_eyes.cee = Meld(MeldStatus.concealed, MeldType.eyes, [w.e, w.e])
wind_eyes.css = Meld(MeldStatus.concealed, MeldType.eyes, [w.s, w.s])
wind_eyes.cww = Meld(MeldStatus.concealed, MeldType.eyes, [w.w, w.w])
wind_eyes.cnn = Meld(MeldStatus.concealed, MeldType.eyes, [w.n, w.n])


# Dragons

dragon_pungs = DotDict()
dregon_pungs.orrr = Meld(MeldStatus.open, MeldType.pung, [d.r, d.r, d.r])
dregon_pungs.oggg = Meld(MeldStatus.open, MeldType.pung, [d.g, d.g, d.g])
dregon_pungs.owww = Meld(MeldStatus.open, MeldType.pung, [d.w, d.w, d.w])

dregon_pungs.crrr = Meld(MeldStatus.concealed, MeldType.pung, [d.r, d.r, d.r])
dregon_pungs.cggg = Meld(MeldStatus.concealed, MeldType.pung, [d.g, d.g, d.g])
dregon_pungs.cwww = Meld(MeldStatus.concealed, MeldType.pung, [d.w, d.w, d.w])

dragon_kongs = DotDict()
dragon_kongs.orrrr = Meld(MeldStatus.open, MeldType.kong, [d.r, d.r, d.r ,d.r])
dragon_kongs.ogggg = Meld(MeldStatus.open, MeldType.kong, [d.g, d.g, d.g, d.g])
dragon_kongs.owwww = Meld(MeldStatus.open, MeldType.kong, [d.w, d.w, d.w, d.w])

dragon_kongs.crrrr = Meld(MeldStatus.concealed, MeldType.kong, [d.r, d.r, d.r ,d.r])
dragon_kongs.cgggg = Meld(MeldStatus.concealed, MeldType.kong, [d.g, d.g, d.g, d.g])
dragon_kongs.cwwww = Meld(MeldStatus.concealed, MeldType.kong, [d.w, d.w, d.w, d.w])

dragon_eyes = DotDict()
dragon_eyes.orr = Meld(MeldStatus.open, MeldType.eyes, [d.r, d.r])
dragon_eyes.ogg = Meld(MeldStatus.open, MeldType.eyes, [d.g, d.g])
dragon_eyes.oww = Meld(MeldStatus.open, MeldType.eyes, [d.w, d.w])

dragon_eyes.crr = Meld(MeldStatus.concealed, MeldType.eyes, [d.r, d.r])
dragon_eyes.cgg = Meld(MeldStatus.concealed, MeldType.eyes, [d.g, d.g])
dragon_eyes.cww = Meld(MeldStatus.concealed, MeldType.eyes, [d.w, d.w])

## Meld Collections

# Chows
coinChows = [c123, c234, c345, c456, c567, c678, c789]
bambooChows = [b123, b234, b345, b456, b567, b678, b789]
characterChows = [k123, k234, k345, k456, k567, k678, k789]
terminalChows = [c123, c789, b123, b789, k123, k789]

# Pungs
coinPungs = [c111, c222, c333, c444, c555, c666, c777, c888, c999]
bambooPungs = [b111, b222, b333, b444, b555, b666, b777, b888, b999]
characterPungs = [k111, k222, k333, k444, k555, k666, k777, k888, k999]
terminalPungs = [c111, c999, b111, b999, k111, k999]
windPungs =  [weee, wsss, wwww, wnnnn]
dragonPungs = [drrr, dggg, dwww]

# Kongs
coinKongs = [c1111, c2222, c3333, c4444, c5555, c6666, c7777, c8888, c9999]
bambooKongs = [b1111, b2222, b3333, b4444, b5555, b6666, b7777, b8888, b9999]
characterKongs = [k1111, k2222, b3333, k4444, b5555, k6666, k7777, k8888, k9999]


