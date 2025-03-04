import time
import sys
import threading
from helper import select_from_choices, clear_terminal
from playsound import playsound


def keys_to_array(dictionary):
    return [key for key in dictionary]


def sleep_for_char(char: str):
    if char == ".":
        time.sleep(0.2)
    elif char == ",":
        time.sleep(0.15)
    elif char == "?":
        time.sleep(0.2)
    elif char == "!":
        time.sleep(0.2)
    else:
        time.sleep(0.05)


def evaluate_condition(condition, user):
    """Evaluate condition as a string and return True/False."""
    try:
        return eval(condition)
    except Exception as e:
        print(f"Error evaluating condition: {e}")
        return False


def typewrite(text: str):
  for char in text:
    print(char, end='', flush=True)
    sleep_for_char(char)

def play_audio(sound):
  audio_file = f"./assets/sounds/{sound}"
  playsound(audio_file)

def parse_dialogue(npc_name, tree, user):
  clear_terminal()
  print(npc_name + ":")

  audio_thread = None
  if "audio" in tree:
    file_name = tree["audio"]
    audio_thread = threading.Thread(target=play_audio, args=(file_name,))
    audio_thread.start()
  
  typewrite(tree["dialogue"])

  if type(tree["responses"]) == type("string"):
    time.sleep(0.5)
    return tree["responses"]

  print("\n")

  valid_responses = {}
  for key, response in tree["responses"].items():
    if "condition" in response:
      if evaluate_condition(response["condition"], user):
        valid_responses[key] = response
    else:
      valid_responses[key] = response

  if not valid_responses:
    return

  choice = select_from_choices(keys_to_array(valid_responses))

  if choice is not None:
    return parse_dialogue(npc_name, valid_responses[choice], user)