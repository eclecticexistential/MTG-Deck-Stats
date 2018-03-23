from play_the_game_output import out_of_all_games
from collect_stats import get_open_hand_stats, get_first_blood_stats, get_mana_starved_stats, get_who_wins_stats


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

limit_2m_2e = Game(40, 2, 2)
limit_2m_2e_open_hand = limit_2m_2e.open_hand()
# limit_2m_2e_first_blood = limit_2m_2e.first_blood()
# limit_2m_2e_mana_starved = limit_2m_2e.mana_starved()
limit_2m_2e_who_wins = limit_2m_2e.who_wins()

# limit_3m_3e = Game(40, 3, 3)
# limit_3m_3e_open_hand = limit_3m_3e.open_hand()
# limit_3m_3e_first_blood = limit_3m_3e.first_blood()
# limit_3m_3e_mana_starved = limit_3m_3e.mana_starved()
# limit_3m_3e_who_wins = limit_3m_3e.who_wins()

print(list(limit_2m_2e_open_hand))
# print(list(limit_3m_3e_open_hand))
# print(list(limit_2m_2e_first_blood))
# print(list(limit_3m_3e_first_blood))
# print(list(limit_2m_2e_mana_starved))
# print(list(limit_3m_3e_mana_starved))
print(list(limit_2m_2e_who_wins))
# print(list(limit_3m_3e_who_wins))



# get_open_hand_stats()
    # get_first_blood_stats()
    # get_who_wins_stats()
    # get_mana_starved_stats()