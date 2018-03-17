import random


def draw(deck, hand):
    try:
        a = random.choice(deck)
    except IndexError:
        return 1
    deck.remove(a)
    hand.append(a)
    return [deck, hand]


def tutor(hand, deck, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    if 66 in hand:
        if mana == 2:
            if land1 >= 1 and land2 >= 1:
                hand.remove(66)
                graveyard.append(66)
                draw(deck, hand)
                draw(deck, hand)
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                return 2
        if mana == 3:
            if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                hand.remove(66)
                graveyard.append(66)
                draw(deck, hand)
                if land1 >= 1 and land2 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                elif land2 >= 1 and land3 >= 1:
                    untapped_mana[1] -= 1
                    untapped_mana[2] -= 1
                elif land3 >= 1 and land1 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[2] -= 1
                return 2


def direct_damage(hand, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    if 13 in hand:
        if mana == 2:
            if land1 >= 1 and land2 >= 1:
                graveyard.append(13)
                hand.remove(13)
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                print("direct damage")
                return 3
        if mana == 3:
            if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                graveyard.append(13)
                hand.remove(13)
                if land1 >= 1 and land2 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                elif land2 >= 1 and land3 >= 1:
                    untapped_mana[1] -= 1
                    untapped_mana[2] -= 1
                elif land3 >= 1 and land1 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[2] -= 1
                print("direct damage")
                return 3


def life_gain(hand, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    if 9 in hand:
        if mana == 2:
            if land1 >= 1 and land2 >= 1:
                hand.remove(9)
                graveyard.append(9)
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                print("life gain")
                return 5
        if mana == 3:
            if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                hand.remove(9)
                graveyard.append(9)
                if land1 >= 1 and land2 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                elif land2 >= 1 and land3 >= 1:
                    untapped_mana[1] -= 1
                    untapped_mana[2] -= 1
                elif land3 >= 1 and land1 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[2] -= 1
                return 5


def removal(hand, field, p1_graveyard, p2_graveyard, untapped_mana, mana, player):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    if 33 in hand:
        if 88 in field:
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    field.remove(88)
                    hand.remove(33)
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                    # opposite player sent to establish who won scenarios...use to distinguish graveyards
                    if player == "P1":
                        p2_graveyard.append(88)
                        p1_graveyard.append(33)
                    elif player == "P2":
                        p1_graveyard.append(88)
                        p2_graveyard.append(33)
                    print("88 was removed")
                    return untapped_mana
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    field.remove(88)
                    hand.remove(33)
                    if land1 >= 1 and land2 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[1] -= 1
                    elif land2 >= 1 and land3 >= 1:
                        untapped_mana[1] -= 1
                        untapped_mana[2] -= 1
                    elif land3 >= 1 and land1 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[2] -= 1
                    if player == "P1":
                        p2_graveyard.append(88)
                        p1_graveyard.append(33)
                    elif player == "P2":
                        p1_graveyard.append(88)
                        p2_graveyard.append(33)
                    print("88 was removed")
                    return untapped_mana
        else:
            pass
    if 13 in hand:
        if 8 in field:
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    field.remove(8)
                    hand.remove(13)
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                    # opposite player sent to establish who won scenarios...use to distinguish graveyards
                    if player == "P1":
                        p2_graveyard.append(8)
                        p1_graveyard.append(13)
                    elif player == "P2":
                        p1_graveyard.append(8)
                        p2_graveyard.append(13)
                    print("8 was removed")
                    return untapped_mana
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    field.remove(8)
                    hand.remove(13)
                    if land1 >= 1 and land2 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[1] -= 1
                    elif land2 >= 1 and land3 >= 1:
                        untapped_mana[1] -= 1
                        untapped_mana[2] -= 1
                    elif land3 >= 1 and land1 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[2] -= 1
                    if player == "P1":
                        p2_graveyard.append(8)
                        p1_graveyard.append(13)
                    elif player == "P2":
                        p1_graveyard.append(8)
                        p2_graveyard.append(13)
                    print("8 was removed")
                    return untapped_mana


def draw_card(deck, hand, graveyard, mana, available_mana):
    a = available_mana[0]
    b = available_mana[1]
    c = available_mana[2]
    if mana == 2:
        if a >= 1 and b >= 1:
            hand.remove(42)
            graveyard.append(42)
            available_mana[0] -= 1
            available_mana[1] -= 1
            print("drew card")
            return draw(deck, hand)
    elif mana == 3:
        if a >= 1 and b >= 1 or b >= 1 and c >= 1 or a >= 1 and c >= 1:
            hand.remove(42)
            graveyard.append(42)
            print("drew card")
            if a >= 1:
                available_mana[0] -= 1
                if b >= 1:
                    available_mana[1] -= 1
                    return draw(deck, hand)
                elif c >= 1:
                    available_mana[2] -= 1
                    return draw(deck, hand)
            elif b >= 1 and c >= 1:
                available_mana[1] -= 1
                return draw(deck, hand)


def play_creature(hand, field, mana, available_mana):
    a = available_mana[0]
    b = available_mana[1]
    c = available_mana[2]
    if mana == 2:
        if a >= 3 and b >= 3:
            if 88 in hand:
                hand.remove(88)
                field.append(88)
                available_mana[0] -= 3
                available_mana[1] -= 3
                return available_mana
        if a >= 1 and b >= 1:
            if 8 in hand:
                hand.remove(8)
                field.append(8)
                available_mana[0] -= 1
                available_mana[1] -= 1
                return available_mana
        else:
            return available_mana
    elif mana == 3:
        if a >= 2 and b >= 2 and c >= 2:
            if 88 in hand:
                hand.remove(88)
                field.append(88)
                available_mana[0] -= 2
                available_mana[1] -= 2
                available_mana[2] -= 2
                return available_mana
        if a >= 1 and b >= 1 and c >= 1:
            if 8 in hand:
                hand.remove(8)
                field.append(8)
                available_mana[0] -= 1
                available_mana[1] -= 1
                available_mana[2] -= 1
                return available_mana
        else:
            return available_mana
