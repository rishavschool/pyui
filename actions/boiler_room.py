from helper import select_from_choices
from dialogues.unc import *
from enemies import Unc
from battles import init_battle
from dialogue_parser import parse_dialogue

def handle_result(result, user):
  if result == "END1": #fight unc
    init_battle(user, Unc())
  elif result == "END2": #nothing happens
    return


def handle_action(user):
  choice = select_from_choices(["Speak to Unc", "Lay on Unc's rock"])

  if choice == "Speak to Unc":
    if user.family == "Unc":
      end = parse_dialogue("Unc", unc_dialogue_unc, user)
      handle_result(end, user)
      
    elif user.family == "Potdar":
      end = parse_dialogue("Unc", unc_dialogue_potdar, user) 
      handle_result(end, user)

    elif user.family == "Ravikanth":
      end = parse_dialogue("Unc", unc_dialogue_ravikanth, user)
      handle_result(end, user)

  elif choice == "Lay on Unc's rock":
    end = parse_dialogue("Unc", unc_dialogue_rock, user)
    handle_result(end, user)