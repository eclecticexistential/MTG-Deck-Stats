from play_the_game_output import out_of_all_games
from collect_stats import get_open_hand_stats, get_first_blood_stats, get_mana_starved_stats, \
    get_who_wins_stats, get_draw_into_win_stats


class Game:
    def __init__(self, cc, mana, evos, special_options=None):
        self.cc = cc
        self.mana = mana
        self.evos = evos
        self.special_ops = special_options  #  for deck customization later
        self.start_game = out_of_all_games(self.cc, self.mana, self.evos)

    def open_hand(self):
        for data in get_open_hand_stats():
            yield data

    def first_blood(self):
        for data in get_first_blood_stats():
            yield data

    def mana_starved(self):
        for data in get_mana_starved_stats():
            yield data

    def who_wins(self):
        for data in get_who_wins_stats():
            yield data

    def draw_steps(self):
        for data in get_draw_into_win_stats():
            yield data


def provide_winner_insight(data, ww=None, wwf=None, wm=None, wr=None, ds=None):
    p1_wins_out_of_games = 0
    p2_wins_out_of_games = 0
    winner_went_first = 0
    winner_went_second = 0
    win_by_combat = 0
    win_by_no_mana = 0
    win_by_milled = 0
    winning_round = []
    for info in data.who_wins():
        if info[3] == 'P1':
            p1_wins_out_of_games += 1
            if info[5] == '0':
                winner_went_first += 1
            elif info[5] == '1':
                winner_went_second += 1
        elif info[3] == 'P2':
            p2_wins_out_of_games += 1
            if info[5] == '1':
                winner_went_first += 1
            elif info[5] == '0':
                winner_went_second += 1
        if info[4] == 'Combat':
            win_by_combat += 1
        elif info[4] == 'NoManaHand' or info[4] == 'ManaStarved':
            win_by_no_mana += 1
        elif info[4] == 'Milled':
            win_by_milled += 1
        if info[2] > 0:
            winning_round.append(info[2])
    if ww:
        return p1_wins_out_of_games/100, p2_wins_out_of_games/100
    if wwf:
        return winner_went_first/100, winner_went_second/100
    if wm:
        return win_by_combat/100, win_by_no_mana/100, win_by_milled/100
    if wr:
        return sum(winning_round)/len(winning_round)
    if ds:
        return data.draw_steps()

# print(list(provide_winner_insight(Game(40, 2, 2), ds=True)))
# limit_3m_3e = Game(40, 3, 3)