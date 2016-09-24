
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
    def __init__(self, tile_type):
        self.type = tile_type
        self.value = -1

    def __init__(self, tile_type, tile_value):
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


# Coins

c1 = Tile(TileType.coin, TileValue.one)
c2 = Tile(TileType.coin, TileValue.two)
c3 = Tile(TileType.coin, TileValue.three)
c4 = Tile(TileType.coin, TileValue.four)
c5 = Tile(TileType.coin, TileValue.five)
c6 = Tile(TileType.coin, TileValue.six)
c7 = Tile(TileType.coin, TileValue.seven)
c8 = Tile(TileType.coin, TileValue.eight)
c9 = Tile(TileType.coin, TileValue.nine)
cr = Tile(TileType.coin, TileValue.red_five)

# Bamboo
b1 = Tile(TileType.bamboo, TileValue.one)
b2 = Tile(TileType.bamboo, TileValue.two)
b3 = Tile(TileType.bamboo, TileValue.three)
b4 = Tile(TileType.bamboo, TileValue.four)
b5 = Tile(TileType.bamboo, TileValue.five)
b6 = Tile(TileType.bamboo, TileValue.six)
b7 = Tile(TileType.bamboo, TileValue.seven)
b8 = Tile(TileType.bamboo, TileValue.eight)
b9 = Tile(TileType.bamboo, TileValue.nine)
br = Tile(TileType.bamboo, TileValue.red_five)


# Characters
k1 = Tile(TileType.character, TileValue.one)
k2 = Tile(TileType.character, TileValue.two)
k3 = Tile(TileType.character, TileValue.three)
k4 = Tile(TileType.character, TileValue.four)
k5 = Tile(TileType.character, TileValue.five)
k6 = Tile(TileType.character, TileValue.six)
k7 = Tile(TileType.character, TileValue.seven)
k8 = Tile(TileType.character, TileValue.eight)
k9 = Tile(TileType.character, TileValue.nine)
kr = Tile(TileType.character, TileValue.red_five)

# Dragons
dr = Tile(TileType.red_dragon)
dg = Tile(TileType.green_dragon)
dw = Tile(TileType.white_dragon)

# Winds
we = Tile(TileType.east_wind)
ws = Tile(TileType.south_wind)
ww = Tile(TileType.north_wind)
wn = Tile(TileType.west_wind)

# Tile Lists

coins = [c1 ,c2, c3, c4, c5, c6, c7, c8, c9, cr]
bamboo = [b1, b2, b3, b4, b5, b6, b7, b8, b9, cr]
characters = [k1, k2, k3, k4, k5, k6, k7, k8, k9, kr]
winds = [we, ws, ww, wn]
dragons = [dr, dg, dw]
terminals = [ c1, c9, b1, b9, k1, k9]
suits = [ *coins, *bamboo, *characters]
honnors = [ *winds, *dragons ]
edges = [ *terminals, *honors]
allTiles = [ *suits, *winds, *dragons ]

