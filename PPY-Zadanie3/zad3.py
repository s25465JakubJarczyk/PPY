import random
import getpass

def get_player_choice(player):
  choice = ''
  while choice not in ['1', '2', '3']:
    choice = getpass.getpass(f"{player}, wybierz: 1 - papier, 2 - nożyce, 3 - kamień: ")
  return int(choice)

def get_computer_choice():
  return random.randint(1, 3)

def get_round_result(player1, player2):
    if player1 == player2:
      return 0
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
      return 1
    else:
      return 2
    
def display_round_result(round_number, player1_name, player1_choice, player2_name, player2_choice, round_result):
  print(f"Runda {round_number}: {player1_name} ({player1_choice}) vs {player2_name} ({player2_choice})")
  if round_result == 0:
    print("Remis!")
  elif round_result == 1:
    print(f"{player1_name} wygrywa rundę!")
  else:
    print(f"{player2_name} wygrywa rundę!")

def display_final_result(player1_name, player2_name, player1_wins, player2_wins):
  print("Wyniki:") 
  print(f"{player1_name}: {player1_wins}") 
  print(f"{player2_name}: {player2_wins}") 
  if player1_wins > player2_wins: 
    print(f"{player1_name} wygrywa grę!") 
  elif player2_wins > player1_wins:
    print(f"{player2_name} wygrywa grę!") 
  else: 
    print("Remis!")
    
def play_game(): 
  print("Witaj w grze Papier Nożyce Kamień!")

  rounds = int(input("Podaj liczbę rund: "))
  
  mode = ''
  while mode not in ['1', '2']:
    mode = input("Wybierz tryb gry: 1 - z komputerem, 2 - hot seats: ")
    
  if mode == '1':
    player1_name = input("Podaj swoje imię: ")
    player2_name = "Komputer"
  else:
    player1_name = input("Podaj imię gracza 1: ") 
    player2_name = input("Podaj imię gracza 2: ")
    
  player1_wins = 0
  player2_wins = 0
  draws = 0
      
      
      
   
