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
    try:
        land1 = untapped_mana[0]
        land2 = untapped_mana[1]
        land3 = untapped_mana[2]
    except TypeError:
        print(hand, field, untapped_mana, player)
    if 33 in hand and 42 in field:
        if mana == 2:
            if land1 >= 1 and land2 >= 1:
                field.remove(42)
                hand.remove(33)
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                # opposite player sent to establish who won scenarios...use to distinguish graveyards
                if player == "P1":
                    p2_graveyard.append(42)
                    p1_graveyard.append(33)
                elif player == "P2":
                    p1_graveyard.append(42)
                    p2_graveyard.append(33)
                # print("42 was removed")
                return
        if mana == 3:
            if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                field.remove(42)
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
                    p2_graveyard.append(42)
                    p1_graveyard.append(33)
                elif player == "P2":
                    p1_graveyard.append(42)
                    p2_graveyard.append(33)
                # print("42 was removed")
                return
