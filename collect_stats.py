open_hands_stats = []
first_blood_stats = []
who_wins_stats = []
mana_starved = []
milled_stats = []
death_by_combat = []


def game_stats(rounds, player, mana, game, hand=None, method=None, winner=None, goes_first=None):
    if hand:
        open_hands_stats.append([mana, game, player, hand])
    if method and winner is None:
        first_blood_stats.append([mana, game, rounds, player, method, goes_first])
    if winner and method is "ManaStarved":
        mana_starved.append([mana, game, rounds, player, goes_first])
    if winner and method is "Milled":
        milled_stats.append([mana, game, rounds, player, goes_first])
    if winner and method is "Combat":
        death_by_combat.append([mana, game, rounds, player, goes_first])
    if method and winner:
        who_wins_stats.append([mana, game, rounds, player, method, goes_first])

