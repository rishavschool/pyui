import time
from helper import *
 

def handle_action(user):
  choice = select_from_choices(["Shake for money", "Pay for food"])

  if choice is None:
    return

  if choice == "Shake for money":
    if chance(35) == True:
      amount = random_between(1, 3)
      user.money += amount
      clear_terminal()
      print(f"You got ${amount} from the vending machine")
      time.sleep(1)

    else:
      clear_terminal()
      print("No money came out of the machine.")
      time.sleep(1)

  elif choice == "Pay for food":
    if user.money >= 1:
      user.money -= 1
      if random_between(1, 2) == 1:
        user.inventory["chips"] += 1
      else:
        user.inventory["soda"] += 1


    else:
      clear_terminal()
      print("You need $1 to buy food")
      time.sleep(1)