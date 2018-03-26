from mtgClasses import *
from collect_stats import game_stats


def dice():
    return random.randint(1, 20)


def create_deck(cards, type_mana, evos=0):
    if evos != 0:
        evo = Deck(cards, Mana(land_type=type_mana, evo=evos))
        return evo
    elif evos == 0:
        non_evo = Deck(cards, Mana(land_type=type_mana))
        return non_evo


def create_hand(deck, cc):
    new_hand = Hand(deck, cc)
    return list(new_hand)


def mulligan(deck, mana, cc, games, player, evos):
    smaller_hand = create_hand(deck, cc)
    return check_hand(smaller_hand, mana, deck, games, player, evos)


def check_hand(hand, mana, deck, games, player, evos=0):
    a = hand.count(2)
    b = hand.count(3)
    c = hand.count(4)
    evo_in_hand = hand.count(10)
    cc = len(hand)
    if cc < 3:
        return False
    if mana == 1:
        if a < 2:
            cc -= 1
            return mulligan(deck, mana, cc, games, player, evos)
    elif mana == 2:
        if a == 0 and b > 0 or a > 0 and b == 0:
            if evo_in_hand > 0:
                game_stats(0, player, mana, games, hand, method=None, winner=None, goes_first=None)
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc, games, player, evos)
        elif a > 0 and b > 0:
            if evos > 0:
                game_stats(0, player, mana, games, hand, method=None, winner=None, goes_first=None)
            elif evos == 0:
                game_stats(0, player, mana, games, hand, method=None, winner=None, goes_first=None)
            return hand
    elif mana == 3:
        if evo_in_hand > 0:
            if a > 0 or b > 0 or c > 0:
                game_stats(0, player, mana, games, hand, method=None, winner=None, goes_first=None)
                return hand
        elif a > 0 and b > 0 or a > 0 and c > 0 or b > 0 and c > 0:
                game_stats(0, player, mana, games, hand, method=None, winner=None, goes_first=None)
                return hand
        else:
            cc -= 1
            return mulligan(deck, mana, cc, games, player, evos)


def open_hand(cards, typemana, games, player, evos=0):
    this_deck = create_deck(cards, typemana, evos)
    a_hand = create_hand(this_deck, 7)
    manad = check_hand(a_hand, typemana, this_deck, games, player, evos)
    if manad:
        curr_deck = list(this_deck)
        for card in manad:
            if card in curr_deck:
                curr_deck.remove(card)
        return [curr_deck, manad]
    else:
        return False


def establish_field(cc, type_mana, games, goes_first, player, evos=0):
    try:
        player_stats = open_hand(cc, type_mana, games, player, evos)
        field = []
        player_stats.append(field)
        graveyard = []
        player_stats.append(graveyard)
        return player_stats
    except AttributeError:
        game_stats(0, player, type_mana, games, hand=None, method="NoManaHand", winner=True, goes_first=goes_first)
        return False


def hand_check(hand, graveyard):
    # discards a 1 to take into account creatures/spells that are played during each round
    if len(hand) > 7:
        if 8 in hand:
            hand.remove(8)
            graveyard.append(8)
            return hand, graveyard
        if 18 in hand:
            hand.remove(18)
            graveyard.append(18)
            return hand, graveyard
