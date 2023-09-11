#!/usr/bin/python3

import json
import sys
import os

def delete_entry_by_title(json_data, title):
    # Load the JSON data
    data = json.loads(json_data)

    # Iterate over the list of items and remove the matching entry
    for idx, item in enumerate(data['items']):
        if item['title'] == title:
            data['items'].pop(idx)
            break

    # Serialize the modified JSON data back to a string
    modified_json_data = json.dumps(data)

    return modified_json_data

# Define the path to the source JSON file as a variable
source_json_file = os.path.join(os.getenv("alfred_workflow_data"), "swatch.json")

# Read JSON data from the file
with open(source_json_file, 'r') as file:
    json_data = file.read()

title_to_delete = sys.argv[1]

modified_json_data = delete_entry_by_title(json_data, title_to_delete)

# Save the modified JSON data back to the file
with open(source_json_file, 'w') as file:
    file.write(modified_json_data)

# Now lets delete the .pngs


hex_code = title_to_delete.lstrip("#")
folder_path = os.path.join(os.getenv("alfred_workflow_data"), "swatch_icons")

files = os.listdir(folder_path)
files_to_delete = [file for file in files if file.startswith(hex_code) and file.lower().endswith(".png")]

for file in files_to_delete:
    file_path = os.path.join(folder_path, file)
    os.remove(file_path)
