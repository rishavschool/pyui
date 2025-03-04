from helper import select_from_choices
from dialogue_parser import parse_dialogue
from dialogues.arav import arav_dialogue

def handle_result(result, user):
  if result == "END1": #nothing
    return
  elif result == "END2":
    user.inventory["polyester scraps"] -= 3
    user.inventory["youngla jeans"] += 1
    return

def handle_action(user):
  choice = select_from_choices(["Speak to Arav"])
  
  if choice == "Speak to Arav":
    end = parse_dialogue("Arav", arav_dialogue, user)
    handle_result(end, user)
