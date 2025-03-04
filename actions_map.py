import importlib
import os

actions_folder = "actions"

actions_map = {}

for filename in os.listdir(actions_folder):
  if filename.endswith(".py") and filename != "__init__.py":
    module_name = filename[:-3]
    location_name = module_name.replace('_', ' ')
    module = importlib.import_module(f"actions.{module_name}")
        
    if hasattr(module, 'handle_action'):
      actions_map[location_name] = module.handle_action