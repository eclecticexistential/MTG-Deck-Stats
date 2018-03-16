import math
import random
from mtgClasses import *
from mtgSpells import draw, tutor, direct_damage, life_gain, removal, play_creature


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


def mulligan(deck, mana, cc):
    smaller_hand = create_hand(deck, cc)
    return check_hand(smaller_hand, mana, deck)


def check_hand(hand, mana, deck):
    a = hand.count(2)
    b = hand.count(3)
    c = hand.count(4)
    evo = hand.count(10)
    cc = len(hand)
    if cc < 3:
        return False
    if mana == 1:
        if a < 2:
            cc -= 1
            return mulligan(deck, mana, cc)
    if mana == 2:
        if a == 0 or b == 0:
            if evo > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)
        else:
            return hand
    if mana == 3:
        if evo > 0:
            if a > 0 and b > 0 or a > 0 and c > 0 or b > 0 and c > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)
        elif evo == 0:
            if a > 0 and b > 0 and c > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)


def open_hand(cards, typemana, evos=0):
    this_deck = create_deck(cards, typemana, evos)
    a_hand = create_hand(this_deck, 7)
    manad = check_hand(a_hand, typemana, this_deck)
    if manad:
        curr_deck = list(this_deck)
        for card in manad:
            if card in curr_deck:
                curr_deck.remove(card)
        return [curr_deck, manad]
    else:
        return False


def establish_field(cc, type_mana, evos=0):
    try:
        player_stats = open_hand(cc, type_mana, evos)
        field = []
        player_stats.append(field)
        graveyard = []
        player_stats.append(graveyard)
        return player_stats
    except AttributeError:
        return False


def hand_check(hand, graveyard):
    # discards a 1 to take into account creatures/spells that are played during each round
    if len(hand) > 7:
        if 8 in hand:
            hand.remove(8)
            graveyard.append(8)
            return hand, graveyard
        if 33 in hand:
            hand.remove(33)
            graveyard.append(33)
            return hand, graveyard


def play_land(mana, deck, hand, field, graveyard):
    d = field.count(2)
    e = field.count(3)
    f = field.count(4)
    snap_shot = [d, e, f]
    if mana == 1:
        field.append(2)
        hand.remove(2)
    if mana == 2:
        if 10 in hand:
            graveyard.append(10)
            hand.remove(10)
            if d >= e:
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif e >= d:
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard, snap_shot, 1
        if d >= e:
            if 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard, snap_shot
        if e >= d:
            if 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard, snap_shot
        if 2 in hand:
            field.append(2)
            hand.remove(2)
            return deck, hand, field, graveyard, snap_shot
        if 3 in hand:
            field.append(3)
            hand.remove(3)
            return deck, hand, field, graveyard, snap_shot
        else:
            return deck, hand, field, graveyard, snap_shot
    elif mana == 3:
        if d > e and e < f:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard, snap_shot
        elif e > d and d < f:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard, snap_shot
        elif f < d and f < e:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 4 in deck:
                    deck.remove(4)
                    field.append(4)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif 4 in hand:
                field.append(4)
                hand.remove(4)
                return deck, hand, field, graveyard, snap_shot
        else:
            if 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard, snap_shot
            elif 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard, snap_shot
            elif 4 in hand:
                field.append(4)
                hand.remove(4)
                return deck, hand, field, graveyard, snap_shot
            else:
                print("made it here")
                return deck, hand, field, graveyard, snap_shot


def check_field(hand, field, evo, mana):
    a = field.count(2)
    b = field.count(3)
    c = field.count(4)
    available_mana = [a, b, c]
    if evo == 1 and a == 1 and b == 1 or a == 3 and b == 3:
        available_mana[0] -= 1
        return play_creature(hand, field, mana, available_mana)
    else:
        return play_creature(hand, field, mana, available_mana)


def check_creatures(battlefield):
    damage = 0
    if 8 in battlefield:
        damage += 1
    elif 88 in battlefield:
        damage += 5
    return damage


def main_phase(hand, deck, field, graveyard, mana):
    was_evo_played = play_land(mana, deck, hand, field, graveyard)
    len_evo = len(was_evo_played)
    snap_shot = was_evo_played[4]
    if len_evo == 6:
        mana_left = check_field(hand, field, 1, mana)
        return hand, deck, field, snap_shot, mana_left
    else:
        mana_left = check_field(hand, field, 0, mana)
        return hand, deck, field, snap_shot, mana_left


def check_snap_shot(x, field):
    a = field.count(2)
    b = field.count(3)
    c = field.count(4)
    field_tots = a + b + c
    mana_stuck = 0
    for x, y in zip(x, x[1:]):
        if x == y:
            mana_stuck += 1
        elif x == 0 and y == 0:
            mana_stuck += 1
    if mana_stuck > 3 and field_tots <= 4:
        print("Mana starved.")
        return 0
    else:
        return 1


def take_turn(deck, hand, graveyard, untapped_mana, opp_field, opp_graveyard, player, life, mana):
    removal(hand, opp_field, graveyard, opp_graveyard, untapped_mana, mana, player)
    if life >= 3:
        tutor(hand, deck, graveyard, untapped_mana, mana)
        return 2
    damage = direct_damage(hand, graveyard, untapped_mana, mana)
    gained = life_gain(hand, graveyard, untapped_mana, mana)
    if damage == 3:
        return damage
    if gained == 5:
        return gained
    else:
        return


def combat_phase(p1_field, p1_life_total, p1_turns, p1_deck, p2_field, p2_life_total, p2_turns, p2_deck):
    # check creatures returns damage based on 8 or 42 (creature size)
    p1_creatures = check_creatures(p1_field)
    p2_creatures = check_creatures(p2_field)

    if p1_creatures > p2_creatures:
        damage = (p1_creatures - p2_creatures) + 1
        p2_life_total -= damage
    elif p1_creatures < p2_creatures:
        damage = (p2_creatures - p1_creatures) + 1
        p1_life_total -= damage

    if p1_life_total <= 0:
        stats = ["P2", p2_turns]
        return stats
    if p2_life_total <= 0:
        stats = ["P1", p1_turns]
        return stats
    if len(p1_deck) == 0:
        stats = ["P2", p2_turns]
        return stats
    if len(p2_deck) == 0:
        stats = ["P1", p1_turns]
        return stats
    else:
        life_status = [p1_life_total, p2_life_total]
        return life_status


def play_the_game(player_one, player_two, mana, goes_first):
    p1_deck, p1_hand, p1_field, p1_grave = player_one
    p2_deck, p2_hand, p2_field, p2_grave = player_two
    p1_turns = 0
    p2_turns = 0
    p1_ss = []
    p2_ss = []
    p1_life = 20
    p2_life = 20

# taking turns... goes_first determines who plays first
    if goes_first == 0:
        while True:
            print()
            print("Start of Round {}.".format(p1_turns +1))
            print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))

            p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
            if p1new_deck == []:
                stats = ["P2", p2_turns]
                return stats
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck, p1_field, p1_grave, mana)
            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                return stats
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    hit = take_turn(p1_deck, p1_hand, p1_grave, p1untapped_mana, p2_field, p2_grave, "P2", p1_life, mana)
                    if hit == 3:
                        p2_life -= 3
                    elif hit == 5:
                        p1_life += 5
                    elif hit == 2:
                        p1_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p1_turns += 1
            else:
                return health
            hand_check(p1_hand, p1_grave)

            p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
            if p2new_deck == []:
                stats = ["P1", p1_turns]
                return stats
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    hit = take_turn(p2_deck, p2_hand, p2_grave, p2untapped_mana, p1_field, p1_grave, "P1", p2_life, mana)
                    if hit == 3:
                        p1_life -= 3
                    elif hit == 5:
                        p2_life += 5
                    elif hit == 2:
                        p2_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p2_turns += 1
            else:
                return health
            hand_check(p2_hand, p2_grave)
    if goes_first == 1:
        while True:
            print()
            print("Start of Round {}.".format(p2_turns +1))
            print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p2_field, p2_hand, p2_grave, p2_life))
            print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p1_field, p1_hand, p1_grave, p1_life))


            p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
            if p2new_deck == []:
                stats = ["P1", p1_turns]
                return stats
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    hit = take_turn(p2_deck, p2_hand, p2_grave, p2untapped_mana, p1_field, p1_grave, "P1", p2_life, mana)
                    if hit == 3:
                        p1_life -= 3
                    elif hit == 5:
                        p2_life += 5
                    elif hit == 2:
                        p2_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p2_turns += 1
            else:
                return health
            hand_check(p2_hand, p2_grave)

            p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
            if p1new_deck == []:
                stats = ["P2", p2_turns]
                return stats
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck, p1_field,
                                                                               p1_grave, mana)
            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                return stats
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    hit = take_turn(p1_deck, p1_hand, p1_grave, p1untapped_mana, p2_field, p2_grave, "P2", p1_life,
                                    mana)
                    if hit == 3:
                        p2_life -= 3
                    elif hit == 5:
                        p1_life += 5
                    elif hit == 2:
                        p1_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p1_turns += 1
            else:
                return health
            hand_check(p1_hand, p1_grave)


def status():
    p1_dice_roll = dice()
    p2_dice_roll = dice()
    goes_first = 0
    if p1_dice_roll < p2_dice_roll:
        goes_first = 1
    return goes_first


def out_of_all_games(cc, mana, evo):
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_draw_steps = []
    games = 100
    while games > 0:
        player_one = establish_field(cc, mana, evo)
        if player_one == False:
            non_evo_wins += 1
            non_evo_draw_steps.append(0)
            games -= 1
        player_two = establish_field(cc, mana)
        if player_two == False:
            evo_wilds_wins += 1
            evo_draw_steps.append(0)
            games -= 1
        elif player_one and player_two:
            goes_first = status()
            winner = play_the_game(player_one, player_two, mana, goes_first)
            # appends num of draws into win condition if player won
            if winner[0] == "P1":
                evo_draw_steps.append(winner[1])
                evo_wilds_wins += 1
                # print("Evo wins")
                games -= 1
            elif winner[0] == "P2":
                non_evo_draw_steps.append(winner[1])
                non_evo_wins += 1
                # print("Non-Evo wins")
                games -= 1

    evo_totes = sum(evo_draw_steps)/len(evo_draw_steps)
    non_evo_totes = sum(non_evo_draw_steps)/len(non_evo_draw_steps)
    print()
    print("Stats for {} Mana Limited Deck \n".format(mana))
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties to Win {}".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(evo_totes))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(non_evo_totes))


out_of_all_games(40, 2, 2)
# out_of_all_games(40, 3, 3)


# magic api starcity,tcg for data sets
# tcg life duration price of card

# lsv hypergeometric calculator
# mtgjson