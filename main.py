import random
from bke import EvaluationAgent, start, can_win, RandomAgent, MLAgent, is_winner, opponent, train, save, load, validate, RandomAgent, plot_validation, RandomAgent, train_and_plot

gamestate = 1

def menu(): 
  print("druk op 1 om het spel te start")

while True:
  print("a: start spel")
  print("b: tegen een andere persoon")
  print("c: tegen een domme tegenstander")
  print("d: tegen een slimme tegenstander")
  print("e: tegenstander later trainen")
  print("f: tegen een getrainde tegenstander")
  print("g: zien hoe goed getrainde tegenstander is")
  print("h: lijngrafiek die progressie van het trainen laat zien")
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
  if i == "f":
    print("You pressed 'f'.")
    gamestate = 6
    break
  if i == "g":
    print("You pressed 'g'.")
    gamestate = 7
    break
  if i == "h":
    print("You pressed 'h'.")
    gamestate = 8
    break
  if i == "i":
    print("You pressed 'i'.")
    gamestate = 9
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

 
class MyAgent(MLAgent):
  def evaluate(self, board):
    
    if is_winner(board, self.symbol):
      reward = 1
      
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
      
    else:
      reward = 0

    return reward

my_agent = MyAgent()      
random_agent = RandomAgent()
if gamestate == 2:
  start()

if gamestate == 3:
  start(player_o = my_random_agent)

if gamestate == 4:
  start(player_o = mijn_speler)

if gamestate == 5: 
  train(my_agent, 3000)
  save(my_agent, 'MyAgent_3000')

if  gamestate == 6:
  my_agent = load('MyAgent_3000')
  my_agent.learning = False
  start(player_x=my_agent)

if gamestate == 7: 
  my_agent = load('MyAgent_3000')
  my_agent.learning = False
  validation_agent = RandomAgent()
  validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
  plot_validation(validation_result)

if gamestate == 8:
  random.seed(1)
  train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)
  