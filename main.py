import random
from bke import EvaluationAgent, start, can_win, RandomAgent

gamestate = 1

def menu(): 
  print("druk op 1 om het spel te start")

while True:
  print("a: start spel")
  print("b: tegen een domme tegenstander")
  print("c: doe zo")
  i = input()  
  
  if i == "a":
    print("You pressed 'a'.")
    gamestate = 1
    break
  if i == "b":
    print("You pressed 'b'.")
    gamestate = 2
    break
menu()

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

results = {"O":0, "X":0, "None":0}
if  gamestate == 1: 
  for i in range(100):
    result = start(player_o = mijn_speler, player_x = my_random_agent)
    
    if result == "X":
      results["X"] += 1
    elif result == "O":
      results["O"] += 1
    else:
      results["None"] += 1

print(results)
  
if gamestate == 2:
  start()