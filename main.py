import random
from bke import EvaluationAgent, start


class MyRandomAgent(EvaluationAgent):
  def evaluatie(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)


  My_random_agent = MyRandomAgent()
start(player_0 = My_Random_Agent)