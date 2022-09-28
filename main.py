import random
from bke import EvaluationAgent, start, can_win, RandomAgent, MLAgent

gamestate = 1

def menu(): 
  print("druk op 1 om het spel te start")

while True:
  print("a: start spel")
  print("b: tegen een andere persoon")
  print("c: tegen een domme tegenstander")
  print("d: tegen een slimme tegenstander")
  i = input()  
  
  if i == "a":
    print("You pressed 'a'.")
    gamestate = 1
    break
  if i == "b":
    print("You pressed 'b'.")
    gamestate = 2
    break
  if i == "c":
    print("You pressed 'c'.")
    gamestate = 3
    break
  if i == "d":
    print("You pressed 'd'.")
    gamestate = 4
    break
  if i == "e":
    print("You pressed 'e'.")
    gamestate = 5
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

class LearningAgent(MLAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    return getal
    
learningagent = LearningAgent

if gamestate == 2:
  start()

if gamestate == 3:
  start(player_o = my_random_agent)

if gamestate == 4:
  start(player_o = mijn_speler)

if gamestate == 5: 
  start(player_o = learningagent)