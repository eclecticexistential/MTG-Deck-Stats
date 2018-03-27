from mtg_evo_wilds_stats import *
from collect_stats import game_stats


def play_the_game(player_one, player_two, mana, goes_first, game_num):
    p1_deck, p1_hand, p1_field, p1_grave = player_one
    p2_deck, p2_hand, p2_field, p2_grave = player_two
    p1_turns = 0
    p2_turns = 0
    p1_ss = []
    p2_ss = []
    p1_life = 20
    p2_life = 20
    round_start = 0
    ticker = 0
    method = ""
# taking turns... goes_first determines who plays first
    if goes_first == 0:
        while True:
            # print()
            # print("Start of Round {}.".format(p1_turns + 1))
            # print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            # print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))
            try:
                p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
            except TypeError:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p1new_deck == []:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats

            p1start_num_creatures = p1_field.count(8)
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck,
                                                                               p1_field, p1_grave, mana)
            p1now_num_creatures = p1_field.count(8)
            p1no_summoning_sickness = p1start_num_creatures - p1now_num_creatures

            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None,
                           method="ManaStarved", winner=True, goes_first=goes_first)
                return stats
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    hit = take_turn(p1_deck, p1_hand, p1_grave, p1untapped_mana, p2_field, p2_grave,
                                    "P2", p1_life, mana)
                    if hit == 3:
                        p2_life -= 3
                        if ticker == 0:
                            method = "Lightning Bolt"
                            ticker += 1
                    elif hit == 5:
                        p1_life += 5
                    elif hit == 2:
                        p1_life -= 2
            if p1no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck,
                                      p1no_summoning_sickness, "P1")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_P2 != p2_life and before_p1 == p1_life and ticker == 0:
                        method == "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat",
                               winner=True, goes_first=goes_first)
                    return health
            p1_turns += 1
            hand_check(p1_hand, p1_grave)

            if p2_life < 20 and ticker == 1:
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker += 1

            ### player two's turn
            try:
                p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
            except TypeError:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p2new_deck == []:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None,
                           method="Milled", winner=True, goes_first=goes_first)
                return stats

            p2start_num_creatures = p2_field.count(8)
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2now_num_creatures = p1_field.count(8)
            p2no_summoning_sickness = p2start_num_creatures - p2now_num_creatures
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="ManaStarved",
                           winner=True, goes_first=goes_first)
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    hit = take_turn(p2_deck, p2_hand, p2_grave, p2untapped_mana, p1_field, p1_grave, "P1", p2_life, mana)
                    if hit == 3:
                        p1_life -= 3
                        if ticker == 0:
                            method = "Lightning Bolt"
                            ticker += 1
                    elif hit == 5:
                        p2_life += 5
                    elif hit == 2:
                        p2_life -= 2
            if p2no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck, p2no_summoning_sickness, "P2")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_p1 != p1_life and before_P2 == p2_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat", winner=True,
                               goes_first=goes_first)
                    return health
            p2_turns += 1
            hand_check(p2_hand, p2_grave)

            if p1_life < 20 and ticker == 1:
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker += 1

    if goes_first == 1:
        while True:
            # print()
            # print("Start of Round {}.".format(p2_turns +1))
            # print("Player2 Field {} Hand {} Graveyard {} Life Total {}".format(p2_field, p2_hand, p2_grave, p2_life))
            # print("Player1 Field {} Hand {} Graveyard {} Life Total {} ".format(p1_field, p1_hand, p1_grave, p1_life))
            try:
                p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
            except TypeError:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p2new_deck == []:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None,
                           method="Milled", winner=True, goes_first=goes_first)
                return stats

            p2start_num_creatures = p2_field.count(8)
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2now_num_creatures = p1_field.count(8)
            p2no_summoning_sickness = p2start_num_creatures - p2now_num_creatures
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="ManaStarved",
                           winner=True, goes_first=goes_first)
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    hit = take_turn(p2_deck, p2_hand, p2_grave, p2untapped_mana, p1_field, p1_grave, "P1", p2_life, mana)
                    if hit == 3:
                        p1_life -= 3
                        if ticker == 0:
                            method = "Lightning Bolt"
                            ticker += 1
                    elif hit == 5:
                        p2_life += 5
                    elif hit == 2:
                        p2_life -= 2
            if p2no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck, p2no_summoning_sickness, "P2")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_p1 != p1_life and before_P2 == p2_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat", winner=True,
                               goes_first=goes_first)
                    return health
            p2_turns += 1
            hand_check(p2_hand, p2_grave)

            # Player Evo's turn
            try:
                p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
            except TypeError:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p1new_deck == []:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats

            p1start_num_creatures = p1_field.count(8)
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck,
                                                                               p1_field, p1_grave, mana)
            p1now_num_creatures = p1_field.count(8)
            p1no_summoning_sickness = p1start_num_creatures - p1now_num_creatures

            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None,
                           method="ManaStarved", winner=True, goes_first=goes_first)
                return stats
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    hit = take_turn(p1_deck, p1_hand, p1_grave, p1untapped_mana, p2_field, p2_grave,
                                    "P2", p1_life, mana)
                    if hit == 3:
                        p2_life -= 3
                        if ticker == 0:
                            method = "Lightning Bolt"
                            ticker += 1
                    elif hit == 5:
                        p1_life += 5
                    elif hit == 2:
                        p1_life -= 2
            if p1no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck,
                                      p1no_summoning_sickness, "P1")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_P2 != p2_life and before_p1 == p1_life and ticker == 0:
                        method == "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat",
                               winner=True, goes_first=goes_first)
                    return health
            p1_turns += 1
            hand_check(p1_hand, p1_grave)

            if p2_life < 20 and ticker == 1:
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker += 1


def status():
    p1_dice_roll = dice()
    p2_dice_roll = dice()
    goes_first = 0
    if p1_dice_roll < p2_dice_roll:
        goes_first = 1
    return goes_first


def out_of_all_games(cc, mana, num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo):
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_draw_steps = []
    games = 100
    while games >= 1:
        goes_first = status()
        if goes_first == 0:
            player_one = establish_field(cc, mana, games, goes_first, "P1", num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo)
            if player_one is False:
                non_evo_wins += 1
                non_evo_draw_steps.append(0)
                games -= 1
            elif player_one:
                player_two = establish_field(cc, mana, games, goes_first, "P2", num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs,)
                if player_two is False:
                    evo_wilds_wins += 1
                    evo_draw_steps.append(0)
                    games -= 1
            if player_one and player_two:
                winner = play_the_game(player_one, player_two, mana, goes_first, games)
                # appends num of draws into win condition if player won
                if winner[0] == "P1":
                    evo_draw_steps.append(winner[1])
                    evo_wilds_wins += 1
                    # print("Evo wins {}".format(games))
                    games -= 1
                elif winner[0] == "P2":
                    non_evo_draw_steps.append(winner[1])
                    non_evo_wins += 1
                    # print("Non-Evo wins {}".format(games))
                    games -= 1
        if goes_first == 1:
            player_two = establish_field(cc, mana, games, goes_first, "P2", num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs)
            if player_two is False:
                evo_wilds_wins += 1
                evo_draw_steps.append(0)
                games -= 1
            elif player_two:
                player_one = establish_field(cc, mana, games, goes_first, "P1", num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo)
                if player_one is False:
                    non_evo_wins += 1
                    non_evo_draw_steps.append(0)
                    games -= 1
            if player_two and player_one:
                winner = play_the_game(player_one, player_two, mana, goes_first, games)
                # appends num of draws into win condition if player won
                if winner[0] == "P1" and winner[1] != 0:
                    evo_draw_steps.append(winner[1])
                    evo_wilds_wins += 1
                    # print("Evo wins {}".format(games))
                    games -= 1
                elif winner[0] == "P2" and winner[1] != 0:
                    non_evo_draw_steps.append(winner[1])
                    non_evo_wins += 1
                    # print("Non-Evo wins {}".format(games))
                    games -= 1

    evo_totes = sum(evo_draw_steps)/len(evo_draw_steps)
    non_evo_totes = sum(non_evo_draw_steps)/len(non_evo_draw_steps)
    game_stats(0, 'all', 0, 100, hand=None, method=None, winner=None, goes_first=None, draws=[evo_totes, non_evo_totes])
    print()
    print("Stats for {} Mana Limited Deck \n".format(mana))
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties to Win {}".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(evo_totes))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(non_evo_totes))

