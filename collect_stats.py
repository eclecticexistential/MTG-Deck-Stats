open_hands_stats = []
first_blood_stats = {}
who_wins_stats = {}
mana_starved = {}


def game_stats(round, player, mana, hand=None, game=None, method=None, winner=None):
    if hand:
        open_hands_stats.append([mana, game, player, hand])
    if winner and method is None:
        mana_starved[round] = player
    if method and winner is None:
        first_blood_stats[round] = [mana, player, method]
    if method and winner:
        who_wins_stats[round] = [player, method]

