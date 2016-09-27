from Tiles import *


class OneYaku:

    class Riichi:
        name = "Riichi"
        english = "Riichi"

        def score(state):
            fan = 0
            if state["riichi"] and state["concealed"]:
                fan += 1
                if state["ippatsu"]:
                    fan += 1

                if state["first_round"]:
                    fan += 1
                print("Riichi Total: %s\n" % fan)
            return fan

    class MenzenTsumo:
        name = "Menzen Tsumo"
        english = "Fully Concealed Hand"

        def score(state):
            fan = 0
            if state["tsumo"] and state["concealed"]:
                fan += 1
                if state["debug"]: print("Menzen Tsumo Total %s\n" % fan)
            return fan

    class TanyaoChuu:
        """
        No terminals or honnors
        """
        name = "Tanyao Chuu"
        english = "All Simples"

        def score(state):
            fan = 0

            if state["concealed"]:
                terminal_or_honnor = False
                for tile in state["tiles"]:
                    if tile in termials:
                        terminal_or_honnor = True
                        break
                if not terminal_or_honnor:
                    fan += 1
                    if state["debug"]: print("Tanyao Chuu %s\n" % fan)


    # Pinfu (Concealed)
    # Four chow and valueless pair. Must declare mahjong on a chow with two-sided wait

    # Iipeiko (Pure Double Chow) (Concealed)
    # Two identical chow of the same suit

    # San shoku doujun (Mixed Triple Chow)
    # Same chow in each suit. +1 additional for concealed hand

    # Itsu (Pure Strait)
    # The three chow 1-3, 4-6, 7-9 of the same suit. +1 additional for concealed hand

    # Fanpai (Dragon Pung)
    # Pung/Kong of dragons

    # Fanpai (Seat/Prevailing Wind)
    # Pung/Kong of seat or prevailing wind

    # Chanta (Outside Hand)
    # All sets contain terminals/honours. At least one chow. +1 Additional for concealed hand.

    # Rinshan Kaihou (After a Kong)
    # Mahjon declared on replacement tile

    # Chan Kan (Robbing a Kong)
    # Mahjong when a pung is extended to kong

    # Haitei (Bottom of the Sea)
    # Mahjong on the last tile, or the following discard







def calculate_fan(tiles, winning, tsumo, ron, seat, prevalent_wind, first_turn, riichi, concealed, first_round, ippatsu, last_tile, debug):
    state = {
        "tiles": tiles,
        "winning": winning,
        "ron": ron,
        "tsumo": tsumo,
        "riichi": riichi,
        "concealed": concealed,
        "first_round": first_round,
        "ippatsu": ippatsu,
        "last_tile": last_tile,
        "seat": seat,
        "prevalent_wind": prevalent_wind,
        "debug": debug
    }

    scores = {}

    scores[OneYaku.Riichi.name] = OneYaku.Riichi.score(state)
    scores[OneYaku.MenzenTsumo.name] = OneYaku.MenzenTsumo.score(state)




    max_score = 0
    max_yaku_name = None

    for k, v in scores.items():
        if v > max_score:
            max_score = v
            max_yaku_name = k

    print("Best Hand:")
    print(" %s %s" % (max_yaku_name, max_score))
    print()





