from colors import TerminalColors
from helper import clear_terminal, select_from_choices
#charisma is like defense, so you take less damage if you are a charismatic guy
#strength is strength u do more damage and stuff

def create_user_name_str(user):
  if type(user).__name__== "Unc":
    return f"{TerminalColors.BOLD}{TerminalColors.BLUE}{TerminalColors.UNDERLINE}Unc {user.name}{TerminalColors.RESET}"
  else:
    return f"{TerminalColors.BOLD}{TerminalColors.BLUE}{TerminalColors.UNDERLINE}{user.name} {type(user).__name__}{TerminalColors.RESET}"

def create_enemy_name_str(enemy):
  return f"{TerminalColors.BOLD}{TerminalColors.RED}{TerminalColors.UNDERLINE}{enemy.name}{TerminalColors.RESET}"


def display_stats(user, enemy, user_health, enemy_health):
  print(create_user_name_str(user))
  print(f"{TerminalColors.BOLD}Health:{TerminalColors.RESET} {TerminalColors.BRIGHT_GREEN}{user_health}/{user.max_health}{TerminalColors.RESET}")
  print("")
  print(create_enemy_name_str(enemy))
  print(f"{TerminalColors.BOLD}Health:{TerminalColors.RESET} {TerminalColors.BRIGHT_GREEN}{enemy_health}/{enemy.max_health}{TerminalColors.RESET}")



def init_battle(user, enemy):
  user_health = user.max_health
  enemy_health = enemy.max_health
  clear_terminal()
  display_stats(user, enemy, user_health, enemy_health)

  print("")
  print(f"It is currently {TerminalColors.BOLD}YOUR{TerminalColors.RESET} turn!")
  
  select_from_choices()
  x = input() #for test