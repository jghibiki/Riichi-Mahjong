import re
from Tiles import *

hand_re = re.compile(r'\[([cbkdw][1-9rwgens])\]')

def parse_hand(hand):
    global hand_re

    # get tile short hands
    m = hand_re.findall(hand)
    tiles = []

    if not m:
        raise Error("Bad hand")

    # translate to tiles
    for tile in m:
        tiles.append(parse_tile(tile))

    return tiles

def parse_winning_tile(tile):
    tile = tile.replace("]", "").replace("[", "")
    return parse_tile(tile)


def parse_tile(tile):

    if tile == "c1":
        return c.t1
    elif tile == "c2":
        return c.t2
    elif tile == "c3":
        return c.t3
    elif tile == "c4":
        return c.t4
    elif tile == "c5":
        return c.t5
    elif tile == "cr":
        return c.tr
    elif tile == "c6":
        return c.t6
    elif tile == "c7":
        return c.t7
    elif tile == "c8":
        return c.t8
    elif tile == "c9":
        return c.t9

    elif tile == "b1":
        return b.t1
    elif tile == "b2":
        return b.t2
    elif tile == "b3":
        return b.t3
    elif tile == "b4":
        return b.t4
    elif tile == "b5":
        return b.t5
    elif tile == "br":
        return b.tr
    elif tile == "b6":
        return b.t6
    elif tile == "b7":
        return b.t7
    elif tile == "b8":
        return c.t8
    elif tile == "b9":
        return b.t9

    elif tile == "k1":
        return k.t1
    elif tile == "k2":
        return k.t2
    elif tile == "k3":
        return k.t3
    elif tile == "k4":
        return k.t4
    elif tile == "k5":
        return k.t5
    elif tile == "kr":
        return k.tr
    elif tile == "k6":
        return k.t6
    elif tile == "k7":
        return k.t7
    elif tile == "k8":
        return k.t8
    elif tile == "k9":
        return k.t9

    elif tile == "dr":
        return d.r
    elif tile == "dg":
        return d.g
    elif tile == "dw":
        return d.w

    elif tile == "we":
        return w.e
    elif tile == "ws":
        return w.s
    elif tile == "ww":
        return w.w
    elif tile == "wn":
        return w.n
    else:
        print("Failed to tile %s" % tile)




