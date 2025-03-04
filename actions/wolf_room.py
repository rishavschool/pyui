from helper import select_from_choices
from dialogue_parser import parse_dialogue
from dialogues.anish import anish_dialogue

def handle_result(result, user):
  if result == "END1": #nothing
    return
  elif result == "END2": #anish gives you aura
    user.inventory["sigma shirt"] += 1



def handle_action(user):
  choice = select_from_choices(["Speak to Anish"])

  if choice == "Speak to Anish":
    end = parse_dialogue("Anish", anish_dialogue, user)
    handle_result(end, user)
