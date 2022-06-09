import random

list = ["Rock", "Paper", "Scissors"]
attempts = 1
attemptsGoal = 1000
RockWin = 0
PaperWin = 0
ScissorsWin = 0
Ties = 0

while True:
  for _ in range(2):
      selection1 = random.choice(list)
      selection2 = random.choice(list)
  
  if selection1 == "Rock" and selection2 == "Paper" or selection2 == "Rock" and selection1 == "Paper":
    PaperWin += 1
    print("(Paper Wins)   " + selection1 + " " + selection2 + "   " + str(attempts))
    
  elif selection1 == "Rock" and selection2 == "Scissors" or selection2 == "Rock" and selection1 == "Scissors":
    RockWin += 1
    print("(Rock Wins)   " + selection1 + " " + selection2 + "   " + str(attempts))
    
  elif selection1 == "Paper" and selection2 == "Scissors" or selection2 == "Paper" and selection1 == "Scissors":
    ScissorsWin += 1
    print("(Scissors Wins)   " + selection1 + " " + selection2 + "   " + str(attempts))
  elif selection1 == selection2:
    Ties += 1
    print("(Tie)   " + selection1 + " " + selection2 + "   " + str(attempts))
  if attempts >= attemptsGoal:
    print("")
    print("Rock Wins: " + str(RockWin))
    print("Paper Wins: " + str(PaperWin))
    print("Scissors Wins: " + str(ScissorsWin))
    print("Ties: " + str(Ties))
    break
  
  attempts += 1
  selection1 = ""
  selection2 = ""
