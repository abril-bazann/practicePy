import random  #random library

#funtions: only runs when its called
def get_choices():
  player_choice = input("Enter a choice (rock,paper,scissors): ")
  options=[ "rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice} #dictionary. it chooses a random choice from the list

  return choices

def check_win(player, computer): #arguments. recieves data
  print(f"you chose {player}, computer chose {computer}") 
  #combine strings and variables together with f

  #refactoring and Nested If. restructuring code while keeping the original funtionality. make the code simpler and easier to read.
  if player==computer:
    return "it's a tie!"  
  elif player=="rock":
    if computer=="scissors": 
      return "rock smashes scissors! you win!"
    else:
      return "paper covers rock! you lose."
  
  elif player=="paper":
    if computer=="rock": 
      return "paper covers rock! you win!"
    else:
      return "scissors cuts paper! you lose."
  
  elif player=="scissors":
    if computer=="paper": 
      return "scissors cuts paper! you lose."
    else:
      return "rock smashes scissors! you lose."

#choices={"player": "rock", "computer": "paper"} 
#p_choice=choices["player"] shows the value of the key
choices=get_choices()
result=check_win(choices["player"], choices["computer"])
print(result) 

