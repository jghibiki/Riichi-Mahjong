from Tiles import *

class MeldStatus:
    revealed = 0
    concealed = 1
    promoted = 2

    reverse = [
        "Revealed",
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


    def compute_statistics():

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
            if(tile.value is TileType.one or
               tile.value is TileType.nine):
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
c123 = Meld(MeldStatus.revealed, MeldType.chow, [c1, c2, c3])
c234 = Meld(MeldStatus.revealed, MeldType.chow, [c2, c3, c4])
c345 = Meld(MeldStatus.revealed, MeldType.chow, [c3, c4, c5])
c34r = Meld(MeldStatus.revealed, MeldType.chow, [c3, c4, cr])
c456 = Meld(MeldStatus.revealed, MeldType.chow, [c4, c5, c6])
c4r6 = Meld(MeldStatus.revealed, MeldType.chow, [c4, cr, c6])
c567 = Meld(MeldStatus.revealed, MeldType.chow, [c5, c6, c7])
cr67 = Meld(MeldStatus.revealed, MeldType.chow, [cr, c6, c7])
c678 = Meld(MeldStatus.revealed, MeldType.chow, [c6, c7, c8])
c789 = Meld(MeldStatus.revealed, MeldType.chow, [c7, c8, c9])

c111 = Meld(MeldStatus.revealed, MeldType.pung, [c1, c1, c1])
c222 = Meld(MeldStatus.revealed, MeldType.pung, [c2, c2, c2])
c333 = Meld(MeldStatus.revealed, MeldType.pung, [c3, c3, c3])
c444 = Meld(MeldStatus.revealed, MeldType.pung, [c4, c4, c4])
c555 = Meld(MeldStatus.revealed, MeldType.pung, [c5, c5, c5])
cr55 = Meld(MeldStatus.revealed, MeldType.pung, [cr, c5, c5])
c5r5 = Meld(MeldStatus.revealed, MeldType.pung, [c5, cr, c5])
c55r = Meld(MeldStatus.revealed, MeldType.pung, [c5, c5, cr])
c666 = Meld(MeldStatus.revealed, MeldType.pung, [c6, c6, c6])
c777 = Meld(MeldStatus.revealed, MeldType.pung, [c7, c7, c7])
c888 = Meld(MeldStatus.revealed, MeldType.pung, [c8, c8, c8])
c999 = Meld(MeldStatus.revealed, MeldType.pung, [c9, c9, c9])

c1111 = Meld(MeldStatus.revealed, MeldType.kong, [c1, c1, c1, c1])
c2222 = Meld(MeldStatus.revealed, MeldType.kong, [c2, c2, c2, c2])
c3333 = Meld(MeldStatus.revealed, MeldType.kong, [c3, c3, c3, c3])
c4444 = Meld(MeldStatus.revealed, MeldType.kong, [c4, c4, c4, c4])
c5555 = Meld(MeldStatus.revealed, MeldType.kong, [c5, c5, c5, c5])
cr555 = Meld(MeldStatus.revealed, MeldType.kong, [cr, c5, c5, c5])
c5r55 = Meld(MeldStatus.revealed, MeldType.kong, [c5, cr, c5, c5])
c55r5 = Meld(MeldStatus.revealed, MeldType.kong, [c5, c5, cr, c5])
cr55r = Meld(MeldStatus.revealed, MeldType.kong, [cr, c5, c5, cr])
c6666 = Meld(MeldStatus.revealed, MeldType.kong, [c6, c6, c6, c6])
c7777 = Meld(MeldStatus.revealed, MeldType.kong, [c7, c7, c7, c7])
c8888 = Meld(MeldStatus.revealed, MeldType.kong, [c8, c8, c8, c8])
c9999 = Meld(MeldStatus.revealed, MeldType.kong, [c9, c9, c9, c9])

c11 = Meld(MeldStatus.revealed, MeldType.eyes, [c1, c1])
c22 = Meld(MeldStatus.revealed, MeldType.eyes, [c2, c2])
c33 = Meld(MeldStatus.revealed, MeldType.eyes, [c3, c3])
c44 = Meld(MeldStatus.revealed, MeldType.eyes, [c4, c4])
c55 = Meld(MeldStatus.revealed, MeldType.eyes, [c5, c5])
cr5 = Meld(MeldStatus.revealed, MeldType.eyes, [cr, c5])
c5r = Meld(MeldStatus.revealed, MeldType.eyes, [c5, cr])
c66 = Meld(MeldStatus.revealed, MeldType.eyes, [c6, c6])
c77 = Meld(MeldStatus.revealed, MeldType.eyes, [c7, c7])
c88 = Meld(MeldStatus.revealed, MeldType.eyes, [c8, c8])
c99 = Meld(MeldStatus.revealed, MeldType.eyes, [c9, c9])


# Bamboos
b123 = Meld(MeldStatus.revealed, MeldType.chow, [b1, b2, b3])
b234 = Meld(MeldStatus.revealed, MeldType.chow, [b2, b3, b4])
b345 = Meld(MeldStatus.revealed, MeldType.chow, [b3, b4, b5])
b34r = Meld(MeldStatus.revealed, MeldType.chow, [b3, b4, br])
b456 = Meld(MeldStatus.revealed, MeldType.chow, [b4, b5, b6])
b4r6 = Meld(MeldStatus.revealed, MeldType.chow, [b4, br, b6])
b567 = Meld(MeldStatus.revealed, MeldType.chow, [b5, b6, b7])
br67 = Meld(MeldStatus.revealed, MeldType.chow, [br, b6, b7])
b678 = Meld(MeldStatus.revealed, MeldType.chow, [b6, b7, b8])
b789 = Meld(MeldStatus.revealed, MeldType.chow, [b7, b8, b9])

b111 = Meld(MeldStatus.revealed, MeldType.pung, [b1, b1, b1])
b222 = Meld(MeldStatus.revealed, MeldType.pung, [b2, b2, b2])
b333 = Meld(MeldStatus.revealed, MeldType.pung, [b3, b3, b3])
b444 = Meld(MeldStatus.revealed, MeldType.pung, [b4, b4, b4])
b555 = Meld(MeldStatus.revealed, MeldType.pung, [b5, b5, b5])
br55 = Meld(MeldStatus.revealed, MeldType.pung, [br, b5, b5])
b5r5 = Meld(MeldStatus.revealed, MeldType.pung, [b5, br, b5])
b55r = Meld(MeldStatus.revealed, MeldType.pung, [b5, b5, br])
b666 = Meld(MeldStatus.revealed, MeldType.pung, [b6, b6, b6])
b777 = Meld(MeldStatus.revealed, MeldType.pung, [b7, b7, b7])
b888 = Meld(MeldStatus.revealed, MeldType.pung, [b8, b8, b8])
b999 = Meld(MeldStatus.revealed, MeldType.pung, [b9, b9, b9])

b1111 = Meld(MeldStatus.revealed, MeldType.kong, [b1, b1, b1, b1])
b2222 = Meld(MeldStatus.revealed, MeldType.kong, [b2, b2, b2, b2])
b3333 = Meld(MeldStatus.revealed, MeldType.kong, [b3, b3, b3, b3])
b4444 = Meld(MeldStatus.revealed, MeldType.kong, [b4, b4, b4, b4])
b5555 = Meld(MeldStatus.revealed, MeldType.kong, [b5, b5, b5, b5])
br555 = Meld(MeldStatus.revealed, MeldType.kong, [br, b5, b5, b5])
b5r55 = Meld(MeldStatus.revealed, MeldType.kong, [b5, br, b5, b5])
b55r5 = Meld(MeldStatus.revealed, MeldType.kong, [b5, b5, br, b5])
b555r = Meld(MeldStatus.revealed, MeldType.kong, [b5, b5, b5, br])
b6666 = Meld(MeldStatus.revealed, MeldType.kong, [b6, b6, b6, b6])
b7777 = Meld(MeldStatus.revealed, MeldType.kong, [b7, b7, b7, b7])
b8888 = Meld(MeldStatus.revealed, MeldType.kong, [b8, b8, b8, b8])
b9999 = Meld(MeldStatus.revealed, MeldType.kong, [b9, b9, b9, b9])

b11 = Meld(MeldStatus.revealed, MeldType.eyes, [b1, b1])
b22 = Meld(MeldStatus.revealed, MeldType.eyes, [b2, b2])
b33 = Meld(MeldStatus.revealed, MeldType.eyes, [b3, b3])
b44 = Meld(MeldStatus.revealed, MeldType.eyes, [b4, b4])
b55 = Meld(MeldStatus.revealed, MeldType.eyes, [b5, b5])
br5 = Meld(MeldStatus.revealed, MeldType.eyes, [br, b5])
b5r = Meld(MeldStatus.revealed, MeldType.eyes, [b5, br])
b66 = Meld(MeldStatus.revealed, MeldType.eyes, [b6, b6])
b77 = Meld(MeldStatus.revealed, MeldType.eyes, [b7, b7])
b88 = Meld(MeldStatus.revealed, MeldType.eyes, [b8, b8])
b99 = Meld(MeldStatus.revealed, MeldType.eyes, [b9, b9])


# Characters
k123 = Meld(MeldStatus.revealed, MeldType.chow, [k1, k2, k3])
k234 = Meld(MeldStatus.revealed, MeldType.chow, [k2, k3, k4])
k345 = Meld(MeldStatus.revealed, MeldType.chow, [k3, k4, k5])
k34r = Meld(MeldStatus.revealed, MeldType.chow, [k3, k4, kr])
k456 = Meld(MeldStatus.revealed, MeldType.chow, [k4, k5, k6])
k4r6 = Meld(MeldStatus.revealed, MeldType.chow, [k4, kr, k6])
k567 = Meld(MeldStatus.revealed, MeldType.chow, [k5, k6, k7])
kr67 = Meld(MeldStatus.revealed, MeldType.chow, [kr, k6, k7])
k678 = Meld(MeldStatus.revealed, MeldType.chow, [k6, k7, k8])
k789 = Meld(MeldStatus.revealed, MeldType.chow, [k7, k8, k9])

k111 = Meld(MeldStatus.revealed, MeldType.pung, [k1, k1, k1])
k222 = Meld(MeldStatus.revealed, MeldType.pung, [k2, k2, k2])
k333 = Meld(MeldStatus.revealed, MeldType.pung, [k3, k3, k3])
k444 = Meld(MeldStatus.revealed, MeldType.pung, [k4, k4, k4])
k555 = Meld(MeldStatus.revealed, MeldType.pung, [k5, k5, k5])
kr55 = Meld(MeldStatus.revealed, MeldType.pung, [kr, k5, k5])
k5r5 = Meld(MeldStatus.revealed, MeldType.pung, [k5, kr, k5])
k55r = Meld(MeldStatus.revealed, MeldType.pung, [k5, k5, kr])
k666 = Meld(MeldStatus.revealed, MeldType.pung, [k6, k6, k6])
k777 = Meld(MeldStatus.revealed, MeldType.pung, [k7, k7, k7])
k888 = Meld(MeldStatus.revealed, MeldType.pung, [k8, k8, k8])
k999 = Meld(MeldStatus.revealed, MeldType.pung, [k9, k9, k9])

k1111 = Meld(MeldStatus.revealed, MeldType.kong, [k1, k1, k1, k1])
k2222 = Meld(MeldStatus.revealed, MeldType.kong, [k2, k2, k2, k2])
k3333 = Meld(MeldStatus.revealed, MeldType.kong, [k3, k3, k3, k3])
k4444 = Meld(MeldStatus.revealed, MeldType.kong, [k4, k4, k4, k4])
k5555 = Meld(MeldStatus.revealed, MeldType.kong, [k5, k5, k5, k5])
kr555 = Meld(MeldStatus.revealed, MeldType.kong, [kr, k5, k5, k5])
k5r55 = Meld(MeldStatus.revealed, MeldType.kong, [k5, kr, k5, k5])
k55r5 = Meld(MeldStatus.revealed, MeldType.kong, [k5, k5, kr, k5])
k555r = Meld(MeldStatus.revealed, MeldType.kong, [k5, k5, k5, kr])
k6666 = Meld(MeldStatus.revealed, MeldType.kong, [k6, k6, k6, k6])
k7777 = Meld(MeldStatus.revealed, MeldType.kong, [k7, k7, k7, k7])
k8888 = Meld(MeldStatus.revealed, MeldType.kong, [k8, k8, k8, k8])
k9999 = Meld(MeldStatus.revealed, MeldType.kong, [k9, k9, k9, k9])

k11 = Meld(MeldStatus.revealed, MeldType.eyes, [k1, k1])
k22 = Meld(MeldStatus.revealed, MeldType.eyes, [k2, k2])
k33 = Meld(MeldStatus.revealed, MeldType.eyes, [k3, k3])
k44 = Meld(MeldStatus.revealed, MeldType.eyes, [k4, k4])
k55 = Meld(MeldStatus.revealed, MeldType.eyes, [k5, k5])
kr5 = Meld(MeldStatus.revealed, MeldType.eyes, [kr, k5])
k5r = Meld(MeldStatus.revealed, MeldType.eyes, [k5, kr])
k66 = Meld(MeldStatus.revealed, MeldType.eyes, [k6, k6])
k77 = Meld(MeldStatus.revealed, MeldType.eyes, [k7, k7])
k88 = Meld(MeldStatus.revealed, MeldType.eyes, [k8, k8])
k99 = Meld(MeldStatus.revealed, MeldType.eyes, [k9, k9])

# Winds

weee = Meld(MeldStatus.revealed, MeldType.pung, [we, we, we])
wsss = Meld(MeldStatus.revealed, MeldType.pung, [ws, ws, ws])
wwww = Meld(MeldStatus.revealed, MeldType.pung, [ww, ww, ww])
wnnn = Meld(MeldStatus.revealed, MeldType.pung, [wn, wn, wn])

weeee = Meld(MeldStatus.revealed, MeldType.kong, [we, we, we ,we])
wssss = Meld(MeldStatus.revealed, MeldType.kong, [ws, ws, ws, ws])
wwwww = Meld(MeldStatus.revealed, MeldType.kong, [ww, ww, ww, ww])
wnnnn = Meld(MeldStatus.revealed, MeldType.kong, [wn, wn, wn, wn])

kee = Meld(MeldStatus.revealed, MeldType.eyes, [we, we])
kss = Meld(MeldStatus.revealed, MeldType.eyes, [ws, ws])
kww = Meld(MeldStatus.revealed, MeldType.eyes, [ww, ww])
knn = Meld(MeldStatus.revealed, MeldType.eyes, [wn, wn])

# Dragons

drrr = Meld(MeldStatus.revealed, MeldType.pung, [dr, dr, dr])
dggg = Meld(MeldStatus.revealed, MeldType.pung, [dg, dg, dg])
dwww = Meld(MeldStatus.revealed, MeldType.pung, [dw, dw, dw])

drrrr = Meld(MeldStatus.revealed, MeldType.kong, [dr, dr, dr ,dr])
dgggg = Meld(MeldStatus.revealed, MeldType.kong, [dg, dg, dg, dg])
dwwww = Meld(MeldStatus.revealed, MeldType.kong, [dw, dw, dw, dw])

drr = Meld(MeldStatus.revealed, MeldType.eyes, [dr, dr])
dgg = Meld(MeldStatus.revealed, MeldType.eyes, [dg, dg])
dww = Meld(MeldStatus.revealed, MeldType.eyes, [dw, dw])

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


