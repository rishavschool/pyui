from helper import select_from_choices

def handle_action(user):
  choice_to_item = {"Steal mayo": "mayo", "Steal sugar": "sugar", "Steal sweetener": "sweetener"}
  choice = select_from_choices(["Steal mayo", "Steal sugar", "Steal sweetener"])

  if not choice in choice_to_item:
    return

  item = choice_to_item[choice]
  if item:
    user.inventory[item] += 1