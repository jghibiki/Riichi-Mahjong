import click
import Parse
from collections import Counter
import Fan


@click.command()
@click.argument("hand")
@click.argument("winning_tile")
@click.option("--tsumo", is_flag=True)
@click.option("--ron", is_flag=True)
@click.option("--seat")
@click.option("--prevalent-wind")
@click.option("--first-turn", is_flag=True)
@click.option("--riichi", is_flag=True)
@click.option("--concealed", is_flag=True)
@click.option("--first-round", is_flag=True)
@click.option("--ippatsu", is_flag=True)
@click.option("--last-tile", is_flag=True)
@click.option("-d/--debug", is_flag=True)
def score_hand(hand, winning_tile, tsumo, ron, seat, prevalent_wind, first_turn, riichi, concealed, first_round, ippatsu, last_tile, d):
    """
    Symbols:
        - Coins:      [cn]
        - Bamboo:     [bn]
        - Characters: [kn]
        - Winds:
            - East:   [we]
            - South:  [ws]
            - West:   [ww]
            - North:  [wn]
        - Dragons:
            - Red:    [dr]
            - Green:  [dg]
            - White:  [dw]

    Note: For suits replace 'n' with the value of the tile. For red fives, replace 'n' with 'r'
    Note: Spaces between tiles may be used to help readability.

    Example Hand:
        '[c1][c2][c3] [dr][dr][dr] [we][we][we] [k1][k2][k3] [br][b5]'
         Hand Contents:
            - Chow of coins 1-3
            - Pung of Red Dragons
            - Pung of East Winds
            - Chow of Characters 1-3
            - Eyes of Bamboo 5 and red 5
    """
    tiles = Parse.parse_hand(hand)
    winning = Parse.parse_winning_tile(winning_tile)

    count = Counter(tiles)
    if d:
        for k in count.keys():
            print("%s %s" % (count[k], k))
        del count
        print("Winning Tile: %s" % winning)
        print()

    Fan.calculate_fan(tiles, winning, tsumo, ron, seat, prevalent_wind, first_turn, riichi, concealed, first_round, ippatsu, last_tile, d)

if __name__ == "__main__":
    score_hand()

