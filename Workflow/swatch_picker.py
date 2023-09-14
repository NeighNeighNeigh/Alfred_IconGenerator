#!/usr/bin/python3

import json
import os
import shutil

alfred_workflow_data = os.getenv("alfred_workflow_data")
alfred_preferences = os.getenv("alfred_preferences")
alfred_workflow_uid = os.getenv("alfred_workflow_uid")

# Set defaults path
defaults_path = os.path.join(alfred_preferences, "workflows", alfred_workflow_uid, "defaults")

# Set input path
input_path = os.path.join(alfred_workflow_data, "swatch.json")


# NOTE: I'm doing this earlier on now, in the first configuration shell script
# # Check if input_path exists
# if not os.path.exists(input_path): # NOTE: I should add a check in here to see if the icon folder exists too
#     # Copy files and folders from defaults_path to alfred_workflow_data
#     shutil.copytree(defaults_path, alfred_workflow_data, dirs_exist_ok=True)


# Read the JSON file
with open(input_path) as file:
    input_json = json.load(file)

# Add workflow data path to the beginning of every icon path
for item in input_json["items"]:
    item["icon"]["path"] = alfred_workflow_data + "/swatch_icons/" + item["icon"]["path"]


# New entry to be added
back = {
    "title": "Back",
    "arg": "back",
    "icon": {
        "path": "back.png"
    }
}

# New entry to be added
add_swatch = {
    "title": "Add Swatch",
    "subtitle": "Hold option to remove a swatch",
    "arg": "new_swatch",
    "icon": {
        "path": "add_swatch.png"
    }
}

# Insert the new entries to the list of items
input_json["items"].insert(0, add_swatch)
input_json["items"].insert(0, back)

# Overflow check
# Check if there are more entries in the list than currently visible
if len(input_json["items"]) > 9:
    # Add "subtitle" to the 7th entry
    input_json["items"][8]["subtitle"] = "Scroll for more swatches…"


json_data = json.dumps(input_json, indent=4)

print(json_data)






