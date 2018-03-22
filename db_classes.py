from play_the_game_output import out_of_all_games
from to_database import get_open_hand_stats, get_first_blood_stats, get_who_wins_stats, get_mana_starved_stats


class Game:
    def __init__(self, cc, mana, evos, special_options=None):
        self.cc = cc
        self.mana = mana
        self.evos = evos
        self.special_ops = special_options  #  for deck customization later
        self.start_game = out_of_all_games(self.cc, self.mana, self.evos)

    def __iter__(self):
        for data in get_open_hand_stats():
            yield data

limit_2m_2e = Game(40, 2, 2)
print(list(limit_2m_2e))
limit_3m_3e = Game(40, 3, 3)
print(list(limit_3m_3e))


# get_open_hand_stats()
    # get_first_blood_stats()
    # get_who_wins_stats()
    # get_mana_starved_stats()