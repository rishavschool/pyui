from colors import TerminalColors
from throwables import throwables
from helper import clear_terminal, select_from_choices

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
  print("")


#repeats until a valid action is selected
def action(*args):
  actions = ["Abilities", "Items"]

  print(f"It is currently {TerminalColors.BOLD}YOUR{TerminalColors.RESET} turn:")
  choice = select_from_choices(actions)

  if choice not in actions:
    clear_terminal()
    display_stats(*args)
    action(*args)
  
  return choice

def items_action(user):
  clear_terminal()
  print("Items:")

  items = []

  for item, quantity in user.inventory.items():
    if quantity > 0 and item in throwables:
      items.append(f"{item.capitalize()}: (Amount: {quantity}) - Damage: {throwables[item]}") #make it display amage nad amount too
  
  items.append("Back")

  choice = select_from_choices(items)

  

#charisma is like defense, so you take less damage if you are a charismatic guy
#strength is strength u do more damage and stuff
def battle_loop(user, enemy, user_health, enemy_health):
  choice = action(user, enemy, user_health, enemy_health) #abilities or items

  if choice == "Abilities":
    pass
  elif choice == "Items":
    items_action(user)



def init_battle(user, enemy):
  user_health = user.max_health
  enemy_health = enemy.max_health
  clear_terminal()
  display_stats(user, enemy, user_health, enemy_health)

  battle_loop(user, enemy, user_health, enemy_health)