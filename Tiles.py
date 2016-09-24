from Utils import DotDict

class TileType:
    coin = 0
    bamboo = 1
    character = 2
    east_wind = 3
    south_wind = 4
    west_wind= 5
    north_wind= 6
    red_dragon = 7
    green_dragon = 8
    white_dragon = 9

    reverse = [
        "Coin",
        "Bamboo",
        "Character",
        "East Wind",
        "South Wind",
        "West Wind",
        "North Wind",
        "Red Dragon",
        "Green Dragon",
        "White Dragon"
    ]


class TileValue:
    one = 0
    two = 1
    three = 2
    four = 3
    five = 4
    six = 5
    seven = 6
    eight = 7
    nine = 8
    red_five = 9

    reverse = [
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Red Five"
    ]


class Tile:
    def __init__(self, tile_type, tile_value=-1):
        self.type = tile_type
        self.value = tile_value


    def __str__(self):
        output = None

        if(self.type == TileType.coin or
           self.type == TileType.bamboo or
           self.type == TileType.characters):
            output = "%s of %ss" % (TileValue.reverse[self.value],
                                    TileType.reverse[self.type])

        else:
            output = TileType.reverse(self.type)

        return output


# coin
c = DotDict()
c.t1 = Tile(TileType.coin, TileValue.one)
c.t2 = Tile(TileType.coin, TileValue.two)
c.t3 = Tile(TileType.coin, TileValue.three)
c.t4 = Tile(TileType.coin, TileValue.four)
c.t5 = Tile(TileType.coin, TileValue.five)
c.t6 = Tile(TileType.coin, TileValue.six)
c.t7 = Tile(TileType.coin, TileValue.seven)
c.t8 = Tile(TileType.coin, TileValue.eight)
c.t9 = Tile(TileType.coin, TileValue.nine)
c.tr = Tile(TileType.coin, TileValue.red_five)

# Bamboo
b = DotDict()
b.t1 = Tile(TileType.bamboo, TileValue.one)
b.t2 = Tile(TileType.bamboo, TileValue.two)
b.t3 = Tile(TileType.bamboo, TileValue.three)
b.t4 = Tile(TileType.bamboo, TileValue.four)
b.t5 = Tile(TileType.bamboo, TileValue.five)
b.t6 = Tile(TileType.bamboo, TileValue.six)
b.t7 = Tile(TileType.bamboo, TileValue.seven)
b.t8 = Tile(TileType.bamboo, TileValue.eight)
b.t9 = Tile(TileType.bamboo, TileValue.nine)
b.tr = Tile(TileType.bamboo, TileValue.red_five)


# Characters
k = DotDict()
k.t1 = Tile(TileType.character, TileValue.one)
k.t2 = Tile(TileType.character, TileValue.two)
k.t3 = Tile(TileType.character, TileValue.three)
k.t4 = Tile(TileType.character, TileValue.four)
k.t5 = Tile(TileType.character, TileValue.five)
k.t6 = Tile(TileType.character, TileValue.six)
k.t7 = Tile(TileType.character, TileValue.seven)
k.t8 = Tile(TileType.character, TileValue.eight)
k.t9 = Tile(TileType.character, TileValue.nine)
k.tr = Tile(TileType.character, TileValue.red_five)

# Dragons
d = DotDict()
d.r = Tile(TileType.red_dragon)
d.g = Tile(TileType.green_dragon)
d.w = Tile(TileType.white_dragon)

# Winds
w = DotDict()
w.e = Tile(TileType.east_wind)
w.s = Tile(TileType.south_wind)
w.w = Tile(TileType.north_wind)
w.n = Tile(TileType.west_wind)

