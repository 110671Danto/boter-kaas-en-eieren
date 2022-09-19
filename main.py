import random
from bke import EvaluationAgent, start, can_win, RandomAgent


class MijnSpeler(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent_symbol):
      getal = getal - 1000

    return getal

class MyrandomAgent(RandomAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1, 500)

my_random_agent = MyrandomAgent()
mijn_speler = MijnSpeler()
start(player_o = mijn_speler, player_x = my_random_agent)